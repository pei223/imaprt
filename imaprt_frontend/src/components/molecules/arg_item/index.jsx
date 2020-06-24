import * as React from 'react';
import Drawer from '@material-ui/core/Drawer';
import IconButton from '@material-ui/core/IconButton';
import BackIcon from '@material-ui/icons/ArrowBack';
import styles from './styles.css'


export default function ArgItem({ type, description, variableName, ...props }) {
    return (
        <li className={styles.container}>
            <span className={styles.variablename}>
                { variableName }
            </span>
            <span className={styles.type}>
                  ({type})  
            </span> - <span  className={styles.description}>{description}</span>
        </li>)
}