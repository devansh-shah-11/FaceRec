# FaceRec - Face Recognition Project

**FaceRec** is an innovative face recognition project utilizing **Flask**, **FastAPI**, **DeepFace**, and **MongoDB** to create a face recognition system. This application allows users to register faces with associated metadata, update their information, and delete data, providing a comprehensive face recognition solution.

<p align="center">
    <a href="https://github.com/devansh-shah-11/FaceRec/actions/workflows/python-app.yml"><img src="https://github.com/devansh-shah-11/FaceRec/actions/workflows/python-app.yml/badge.svg" alt="Python application"></a>
    <a href="https://github.com/devansh-shah-11/FaceRec/actions/workflows/codeql.yml"><img src="https://github.com/devansh-shah-11/FaceRec/actions/workflows/codeql.yml/badge.svg" alt="CodeQL"></a>
    <a href="https://codecov.io/gh/devansh-shah-11/FaceRec"><img src="https://codecov.io/gh/devansh-shah-11/FaceRec/branch/main/graph/badge.svg" alt="codecov"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=alert_status" alt="Quality Gate Status"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=bugs" alt="Bugs"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=code_smells" alt="Code Smells"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=ncloc" alt="Lines of Code"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=security_rating" alt="Security Rating"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=sqale_rating" alt="Sqale Rating"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=sqale_index" alt="Sqale Index"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=reliability_rating" alt="Reliability Rating"></a>
    <a href="https://sonarcloud.io/dashboard?id=Devasy23_FaceRec"><img src="https://sonarcloud.io/api/project_badges/measure?project=Devasy23_FaceRec&metric=vulnerabilities" alt="Vulnerabilities"></a>
</p>

## 🚀 Features

- **Real-Time Face Recognition:** Detect and recognize faces seamlessly in real-time.
- **User-Friendly Interface:** Clean design for enhanced user experience.
- **Metadata Management:** Register, update, and delete face entries with ease.
- **Scalable Architecture:** Built to handle multiple users and extensive datasets.

## 📊 Repository Statistics

| Metric                  | Badge                                                                                           | Link                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Stars**               | ![GitHub Stars](https://img.shields.io/github/stars/Devasy23/FaceRec?style=social)             | [Stars](https://github.com/Devasy23/FaceRec/stargazers)                                 |
| **Forks**               | ![GitHub Forks](https://img.shields.io/github/forks/Devasy23/FaceRec?style=social)             | [Forks](https://github.com/Devasy23/FaceRec/network/members)                            |
| **Open Issues**         | ![GitHub Issues](https://img.shields.io/github/issues/Devasy23/FaceRec)                        | [Issues](https://github.com/Devasy23/FaceRec/issues)                                    |
| **Open Pull Requests**  | ![GitHub PRs](https://img.shields.io/github/issues-pr/Devasy23/FaceRec)                        | [Pull Requests](https://github.com/Devasy23/FaceRec/pulls)                              |
| **Closed Pull Requests**| ![GitHub Closed PRs](https://img.shields.io/github/issues-pr-closed/Devasy23/FaceRec)          | [Closed PRs](https://github.com/Devasy23/FaceRec/pulls?q=is%3Apr+is%3Aclosed)           |

## 📦 Getting Started

These instructions will guide you through setting up the project on your local machine for development.

### Prerequisites

Make sure you have **Python 3.10 or later** installed.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Devasy23/FaceRec.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd FaceRec
   ```

3. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

To start the Flask and FastAPI applications, run:
```bash
python main.py
```

Your application will be available at `http://localhost:5000`.

<details>
<summary><strong>Project Structure</strong></summary>

- `requirements.txt`: Contains the Python dependencies for the project.
- `API/`: FastAPI application code.
- `FaceRec/`: HTML, CSS, and Flask application files.
- `Model-Training/`: Scripts for model training.
- `docs/`: Documentation files.
- `test-faces/`: Test data for face recognition.
- `main.py`: Code to start FastAPI and Flask applications.

</details>


## Sequence Diagram

![image.png](sequence-diagram.png)


## 🗄️ Database Schema

1. **Create a New MongoDB Connection** using:
   ```
   mongodb://localhost:27017/8000
   ```

2. **Database Details:**
   - **Database Name**: `DatabaseName`
   - **Collection Name**: `CollectionName`

3. **Import Data**:
   - From the `database.mongo` folder -> `{DatabaseName}.{CollectionName}.json`

### The `faceEntries` Collection Schema:

- `id`: Unique identifier for the face entry.
- `Employeecode`: Unique employee ID associated with the image.
- `Name`: Person's name.
- `Gender`: Gender of the person.
- `Department`: Department of the person.
- `time`: Timestamp of the face entry creation.
- `embeddings`: Embeddings of the face image.
- `Image`: Base64 encoded image file.

## 🔄 Function Flow

1. **`create_new_faceEntry()`**: Receives a POST request with an image and metadata, extracts the face, calculates embeddings, and stores data in the database.
2. **`Data()`**: Sends a GET request to the `/data` endpoint to retrieve the list of face entries from MongoDB.
3. **`update()`**: Updates the details of a face entry in the database.
4. **`read()`**: Sends a GET request with a specific `Employeecode` to retrieve related information.
5. **`delete()`**: Deletes specific employee data from the database.

## 🧪 Testing

To run the tests:
```bash
pytest
```

## 👥 Our Valuable Contributors ❤️✨
Thanks to all the amazing people who have contributed to **FaceRec**! 💖

[![Contributors](https://contrib.rocks/image?repo=Devasy23/FaceRec)](https://github.com/Devasy23/FaceRec/graphs/contributors)

## 📄 Documentation

For detailed API documentation, refer to the [API Documentation](API_DOCUMENTATION.md) file.

## 📄 License

This project is licensed under the **Apache License**. See the [LICENSE](LICENSE) file for details.