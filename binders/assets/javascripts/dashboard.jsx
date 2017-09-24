// @flow
"use strict";

import _ from 'lodash';
import Pagination from 'react-bootstrap';
import React from 'react';
import ReactDOM from 'react-dom';
import DataTable from './components/datatable.jsx';

//TODO: make this configurable
const paginationRowCount = 10;

const tableData = [];
const columnInfo = [];


class Dashboard extends React.PureComponent {
    constructor() {
        super();
        this.state = {
            displayData: _.slice(tableData, 0, paginationRowCount),
            currentPage: 1
        }
    }

    setCurrentPage(event, selectedEvent) {
        let startValue = (selectedEvent.eventKey - 1) * paginationRowCount;
        this.setState({
            currentPage: selectedEvent.eventKey,
            displayData: _.slice(tableData, startValue, startValue + paginationRowCount)
        })
    }

    render() {
      let addNumber = tableData.length % paginationRowCount === 0 ? 0 : 1;
      let pageCount = _.floor((tableData.length / paginationRowCount) + addNumber);

      return (
        <div>
            <DataTable data={this.state.displayData} columnInfo={columnInfo}/>
            <div className="pagination-container">
                <Pagination
                    prev
                    next
                    first
                    last
                    ellipsis
                    items={pageCount}
                    maxButtons={5}
                    activePage={this.state.currentPage}
                    onSelect={this.setCurrentPage.bind(this)}
                    />
            </div>
        </div>
      )
    }
}

ReactDOM.render(
    <Dashboard />,
    document.getElementById('dashboard-container')
);
