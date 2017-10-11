// @flow
"use strict";
import React from "react";
import ReactDOM from "react-dom";
import { Autocomplete }   from 'material-ui';


class SearchPanel extends React.PureComponent {

  constructor(props) {
    super(props);
  }

  onSearchChanged() {
    let query = ReactDOM.findDOMNode(this.refs.search).value;
    this.props.onSearchChanged(query);
  }

  render() {
    return (
      <div className="row">
        <div className="one-fourth column">
          Filter: &nbsp;
          <input ref='search' type='text' value={this.props.search} onChange={this.onSearchChanged} />
          {this.props.search?<button onClick={this.props.onClearSearch} >x</button>:null}
        </div>
      </div>
    )
  }
}

export default SearchPanel;
