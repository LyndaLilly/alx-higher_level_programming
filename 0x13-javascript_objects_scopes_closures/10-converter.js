#!/usr/bin/node

exports.converter = function (base) {
  return function (res) {
    return res.toString(base);
  };
};
