import styles from './Start.module.css';
import React, { useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';

function Body() {
    const labelStyle = {
        cursor: 'pointer'
    };

    return (
        <div className={styles.start}>
            <label id="initial" style={labelStyle}>Zô</label>
        </div>
    );
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
        const label = document.getElementById("initial");
        label.addEventListener("click", handelClick);

        // Cleanup the event listener when the component unmounts
        return () => {
            label.removeEventListener("click", handelClick);
        };
    }, [handelClick]);

    return <Body />;
}

export default function Start() {
    return (
        <div className={styles.all}>
            <Click />
        </div>
    );
}
