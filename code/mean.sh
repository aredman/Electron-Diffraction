#!/bin/bash

cut -d';' -f 1 $1 | paste -s -d '+'
