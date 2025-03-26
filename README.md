# Technical Challenge

## Description
This repository contains solutions to the technical challenge. 

## Requirements
- Python 3.12.4
- Internet connection for querying the API in Exercise 2
- Dependencies specified in `requirements.txt`

### Dependencies Classification
- **HTTP Requests**: `requests==2.28.2`
- **Database Connection**: `mysql-connector-python`
- **Environment Variables Management**: `python-dotenv`

## Install Dependencies
Before running the scripts, install the required dependencies with:
```bash
pip install -r requirements.txt
```

## Repository Structure
```
📂 Technical_Challenge
│── 📝 README.md
│── 📄 requirements.txt
│── 📄 Minesweeper.py
│── 📄 Rest_API.py
│── 📄 Create-Insert.py
│── 📄 ReporteSQL.py
```

## Exercises

### 1. Minesweeper: Number of Neighboring Mines
#### Description:
A function must be created that takes a list representation of a Minesweeper board and returns another board where the value of each cell represents the number of neighboring mines.

#### File:
[Minesweeper.py](Minesweeper.py)

---

### 2. REST API: Best TV Shows by Genre
#### Description:
The HTTP GET method must be used to retrieve information about recent television shows by querying the API `https://jsonmock.hackerrank.com/api/tvseries`. The query is paginated, so to access additional pages, append `?page={num}` to the URL.

#### File:
[Rest_API.py](Rest_API.py)

---

### 3. SQL: Database Creation and Query
#### a) Database Creation and Data Insertion
Defines the structure of the database and populates it with relevant data.

#### File:
[Create-Insert.py](Create-Insert.py)

#### b) Advertising System Failures Report
As part of HackerAd's advertising system analytics, a team needs a list of customers who have more than 3 events with status "failure" in their campaigns. The result must include the customer's full name and the number of failures.

#### File:
[ReporteSQL.py](ReporteSQL.py)

## How to Run
1. **Exercise 1 (Minesweeper):**
   ```bash
   python Minesweeper.py
   ```
2. **Exercise 2 (REST API):**
   ```bash
   python Rest_API.py
   ```
3. **Exercise 3 (Database and SQL Report):**
   - Run `Create-Insert.py` to create tables and insert data:
     ```bash
     python Create-Insert.py
     ```
   - Run `ReporteSQL.py` to generate the report:
     ```bash
     python ReportSQL.py
     ```
