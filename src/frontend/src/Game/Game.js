import styles from './Game.module.css';
import React, { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';

function ProductName() {
    return (
        <div className={styles.productName}>
            <label>Connect Từ</label>
            {/* Copyright by Squiggly Text https://codepen.io/lbebber/pen/KwGEQv */}
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
                <defs>
                    <filter id="squiggly-0">
                        <feTurbulence id="turbulence" baseFrequency="0.02" numOctaves="3" result="noise" seed="0"/>
                        <feDisplacementMap id="displacement" in="SourceGraphic" in2="noise" scale="6" />
                    </filter>
                    <filter id="squiggly-1">
                        <feTurbulence id="turbulence" baseFrequency="0.02" numOctaves="3" result="noise" seed="1"/>
                <feDisplacementMap in="SourceGraphic" in2="noise" scale="8" />
                    </filter>
                    
                    <filter id="squiggly-2">
                        <feTurbulence id="turbulence" baseFrequency="0.02" numOctaves="3" result="noise" seed="2"/>
                <feDisplacementMap in="SourceGraphic" in2="noise" scale="6" />
                    </filter>
                    <filter id="squiggly-3">
                        <feTurbulence id="turbulence" baseFrequency="0.02" numOctaves="3" result="noise" seed="3"/>
                <feDisplacementMap in="SourceGraphic" in2="noise" scale="8" />
                    </filter>
                    
                    <filter id="squiggly-4">
                        <feTurbulence id="turbulence" baseFrequency="0.02" numOctaves="3" result="noise" seed="4"/>
                <feDisplacementMap in="SourceGraphic" in2="noise" scale="6" />
                    </filter>
                    </defs> 
            </svg>
        </div>
    );
}

function Count({ count }) {
    return (
      <div className={styles.count}>
        <label id="count">{count}</label>
      </div>
    );
  }

function Top({ count }) {
    return (
        <div className={styles.top}>
        <ProductName />
        <Count count={count} />
        </div>
    );
}

function ComAns({ outputLabel }) {
    return (
        <div className={styles.answer}>
            <label id="outputLabel">{outputLabel}</label>
        </div>
    );
 }

function Suggest({ compJoke }) {
    return (
      <div className={styles.suggest}>
        <label id="compJoke">{compJoke}</label>
      </div>
    );
  }
  
function UsrAns() {
    const [count, setCount] = useState(3);
    const [usrInput, setUsrInput] = useState('');
    const [compJoke, setCompJoke] = useState('');
    const [outputLabel, setOutputLabel] = useState('Mời bạn đi trước');
    const navigate = useNavigate();

    const handleRepeatvalue = useCallback((event) => {
        event.preventDefault();

        setCompJoke('');
        setUsrInput(usrInput.trim());
    
        // Check if user input is empty
        if (!usrInput) {
            setCompJoke('Điền từ vào!!!');
            setUsrInput('');
            setCount(count - 1);

            return false;
        }
    
        const compOut = outputLabel.split(' ');
        const usrOut = usrInput.split(' ');
    
        // Check if user input matches the expected word
        if (compOut.length === 2 && usrOut[0] !== compOut[1]) {
            setCompJoke('Chơi gì kì zậy!');
            setUsrInput('');
            setCount(count - 1);

            return false;
        } else {
            // Make an asynchronous request to check the word
            const requestOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'input': usrInput,
                }),
                redirect: 'follow',
            };
    
            fetch('http://127.0.0.1:5002/process', requestOptions)
            .then((response) => response.json())
            .then((result) => {
                const output = result.output;
                const check = result.check;
                const lose = result.lose;
    
                if (!lose) {
                    if (!check) {
                        setCompJoke('Từ này dùng rồi mà!');
                        setUsrInput('');
                        setCount(count - 1);
                    } else {
                        setOutputLabel(output);
                    }
                } else {
                    navigate("/win");
                }
            })
            .catch((error) => {
                console.log('error', error);
                setCompJoke('Có chút lỗi. Vui lòng nhập lại!');
            });
        }
    
        setUsrInput('');
    
        return false;
    }, [navigate, count, usrInput, outputLabel]);
  
    if (count === 0) {
        navigate('/lose');
    }

    return (
        <div className={styles.container}>
            <Top count={count} />
            <ComAns outputLabel={outputLabel} />
            <div className={styles.centerScreen}>
                <form onSubmit={handleRepeatvalue}>
                    <input
                        type="text"
                        className={styles.largeInput}
                        onChange={(e) => setUsrInput(e.target.value)}
                    />
                </form>
            </div>
            <Suggest compJoke={compJoke} />
        </div>
    );
}

export default function Game() {
    return (
        <UsrAns />
    );
}