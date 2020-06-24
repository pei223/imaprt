import * as React from 'react';
import FilterHelpItem from '../../molecules/filter_help_item'


export default function FilterHelpView({ filterHelpList, ...props }) {
    return (
        <div>
            <h1>フィルターのヘルプ</h1>
            {filterHelpList.map((item) => {
                return <FilterHelpItem key={item.filterName} filterName={item.filterName} overview={item.overview} argList={item.argList}  />
            })}
        </div>)
}