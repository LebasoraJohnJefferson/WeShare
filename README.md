# WeShare

<div align='center'>
    <div>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHLxxSOS1EacExleh0u6endvPLIbPd8vC_wQ&usqp=CAU' alt='python' style='width:5rem; height:5rem;border-radius:.3rem;'>
        <br>
        <h2>project in python</h2>
    </div>
</div>


## Getting Started

Install project dependencies:

```bash
pip install -r requirement.txt
```

Create a required environment variable:

```bash
echo SECRET_KEY=your-secret-key > .env
```

Migration configurations:

```bash
py manage.py makemigrations
py manage.py migrate --run-syncdb
```

Start development server:

```bash
py manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.
