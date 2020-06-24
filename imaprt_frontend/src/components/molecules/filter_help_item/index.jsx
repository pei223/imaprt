import * as React from 'react';
import styles from './styles.css'
import ArgItem from '../arg_item'


export default function FilterHelpItem({ filterName, overview, argList, ...props }) {
    const [more, setMore] = React.useState(false)
    
    return (
        <div className={styles.container}>
            <h2 className={styles.filtername} onClick={() => setMore(!more)}>{filterName}</h2>
            <div className={styles.detailarea} style={{display: more ? "block" : "none"}}>
                <p className={styles.overview}>
                    {overview}
                </p>
                <h4 className={styles.headline}>Params</h4>
                <div className={styles.argsarea}>
                    {argList.map((item) => {
                        return <ArgItem key={item.variableName} type={item.type} description={item.description} variableName={item.variableName}  />
                    })}
                </div>
            </div>
        </div>)
}