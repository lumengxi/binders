// @flow
"use strict";

import React from 'react';
import { Cell } from 'fixed-data-table';

export default class LinkCell extends React.PureComponent {

  static propTypes = {
    data: React.PropTypes.array.isRequired,
    field: React.PropTypes.string.isRequired,
  };

  render() {
    const { rowIndex, field, data, ...props } = this.props;
    const link = '/domain/' + data[rowIndex].id;
    return (
      <Cell {...props}>
       <a href={link}>{data[rowIndex].name}</a>
      </Cell>
    );
  }
}