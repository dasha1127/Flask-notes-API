# Flask Notes API

This is a simple REST API built using **Python** and **Flask**.
It allows users to create, view, and delete notes.

---

## Features

* Create a note (POST /notes)
* Get all notes (GET /notes)
* Get a single note (GET /notes/<id>)
* Delete a note (DELETE /notes/<id>)

---

## Technologies Used

* Python
* Flask
* Postman (for API testing)

---

## How to Run the Project

1. Install Flask:

```
pip install flask
```

2. Run the application:

```
python app.py
```

3. Open in browser:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### 1. Create Note

**POST** `/notes`

Body (JSON):

```
{
  "text": "My first note"
}
```

---

### 2. Get All Notes

**GET** `/notes`

---

### 3. Get One Note

**GET** `/notes/<id>`

Example:

```
/notes/1
```

---

### 4. Delete Note

**DELETE** `/notes/<id>`

---

Screenshots

Screenshots of API requests and responses are included in the `screenshots` folder.

---

## Author

**GitHub:** [https://github.com/dasha1127](https://github.com/dasha1127)
