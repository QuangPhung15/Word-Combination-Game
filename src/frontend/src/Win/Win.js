import styles from './Win.module.css';
import Game from '../Game/Game.js';
import React, { useEffect, useState } from 'react';

function State() {
    return (
        <div className={styles.win}>
            <label>Thắng Rồi!!!!!</label>
        </div>
    );
}

function Replay() {
    const labelStyle = {
        cursor: 'pointer'
    };

    return ( 
        <div className={styles.replay}>
            <label id="playAgain" style={labelStyle}>Chơi Lại</label>
        </div>
    );
}

function Effect() {
    return (
        // Copyright by Squiggly Text https://codepen.io/lbebber/pen/KwGEQv
        <div className={styles.confetti}>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
            <div className={styles.confetti-piece}></div>
        </div>
    )
}


function Body() {
    return (
        <>
            <State />
            <Replay />
            <Effect />
        </>
    )
}

function Click() {
    const [click, setClick] = useState(false);

    function handelClick() {
        var raw = "";

        var requestOptions = {
            method: 'POST',
            body: raw,
            redirect: 'follow'
        };

        fetch("http://127.0.0.1:5002/start", requestOptions)
            .then(response => response.text())
            .then(result => setClick(true))
            .catch(error => console.log('error', error));
        
        setClick(true)

        return false;
        
    }

    useEffect(() => {
        const label = document.getElementById("playAgain");
        label.addEventListener("click", handelClick);

        // Cleanup the event listener when the component unmounts
        return () => {
            label.removeEventListener("click", handelClick);
        };
    }, []);

    if (click) {
        return <Game />;
    }

    return <Body />;
}

export default function Win() {
    return (
        <Click />
    );
}