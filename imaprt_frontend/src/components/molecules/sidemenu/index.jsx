import * as React from 'react';
import Drawer from '@material-ui/core/Drawer';
import IconButton from '@material-ui/core/IconButton';
import BackIcon from '@material-ui/icons/ArrowBack';
import styles from './styles.css'


export default function SideMenu({children, open, onClose, width, variant="persistent", ...props}) {
    return (
    <Drawer open={open} onClose={onClose} anchor={"right"} variant={variant}>
        <div style={{width: width}} className={styles.contentarea}>
            <p className={styles.headerarea} style={{paddingRight: "10px", paddingLeft: "10px", paddingBottom: "10px"}}>
                <IconButton onClick={onClose}>
                    <BackIcon />
                </IconButton>
            </p>
            <div className={styles.helplistarea}>
                { children }
            </div>
        </div>
    </Drawer>)
}