#!/bin/bash

clear; rm db.sql; python create_db.py; python insert_db.py; python insert_db.py; python read_db.py;
