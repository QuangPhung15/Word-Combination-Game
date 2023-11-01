import styles from './Lose.module.css';
import React, { useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';

function State() {
    return (
        <div className={styles.lose}>
            <label>Thua Rồi!!!!</label>
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


function Body() {
    return (
        <div className={styles.container}>
            <State />
            <Replay />
        </div>
    )
}

function Click() {
    const navigate = useNavigate();

    const handelClick = useCallback(() => {
        var raw = "";

        var requestOptions = {
            method: 'POST',
            body: raw,
            redirect: 'follow'
        };

        fetch("http://127.0.0.1:5002/start", requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));

        navigate('/game');

        return false;
    }, [navigate]);

    useEffect(() => {
        const label = document.getElementById("playAgain");
        label.addEventListener("click", handelClick);

        // Cleanup the event listener when the component unmounts
        return () => {
            label.removeEventListener("click", handelClick);
        };
    }, [handelClick]);

    return <Body />;
}

export default function Lose() {
    return (
        <div className={styles.all}>
            <Click />
        </div>
    );
}