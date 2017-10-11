// @flow
"use strict";
import React from "react";

const $ = require("jquery");

export const FETCH_ALL_DOCUMENTATIONS = "FETCH_ALL_DOCUMENTATIONS";

export function fetchAllDocumentations() {
  return function (dispatch) {
    dispatch(fetchAllDocumentations());

    $.ajax({
      type: "GET",
      dataType: ""
    })
  };
}