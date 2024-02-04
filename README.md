# Pokémon Project

## Project Overview

This Django-based project provides an interface to interact with the PokeAPI, displaying various details about Pokémon, including their names, types, heights, and weights. It features lists of Pokémon filtered by specific criteria, such as weight ranges or types, and includes functionality to display Pokémon names in reverse. The project also utilizes Tailwind CSS, that require Node.js packages managed through NPM.

[Video demonstration](https://youtu.be/hBqttWWpJSE)

## Features

- **List Display**: Showcases a paginated list of the first 50 Pokémon with detailed information.
- **Weight and Height Filter**: Filters Pokémon by a specified weight or height range (e.g., 30 to 80 units).
- **Type Filter**: Displays Pokémon of specific types such as Grass or Flying.
- **Reverse Names**: Offers a view that lists Pokémon with their names reversed.
- **Concurrency**: Utilizes Python concurrency for efficient data retrieval from the PokeAPI.
- **Front-end Interactivity**: Enhances user experience with Tailwind CSS.

## Installation

### Python and Django Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/mtumalan/pokedex.git
    cd pokedex
    ```

2. **Set Up a Virtual Environment**

    - For Unix/macOS:
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```

    - For Windows:
        ```cmd
        py -m venv env
        .\env\Scripts\activate
        ```

3. **Install Python Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Node.js and NPM Setup

1. **Install Node.js and NPM**

    Ensure you have Node.js and NPM installed on your system. You can download them from [nodejs.org](https://nodejs.org/).

2. **Install Node.js Dependencies**

    Navigate to the project directory and install the required Node.js packages defined in `package.json`:

    ```bash
    npm install
    ```

    This command installs all the necessary NPM packages for the project.

## Running the Project

1. **Migrate the Database**

    ```bash
    python manage.py migrate
    ```

2. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    Access the web application at [http://127.0.0.1:8000/pokemons](http://127.0.0.1:8000/pokemons/).

3. **Build Front-end Assets**

    To apply Tailwind CSS compilation, run:

    ```bash
    npm run build
    ```

## Usage

- Navigate to the homepage to view the list of the first 50 Pokémon.
- Use the menu to access different filtered lists based on weight, type, or to see reversed Pokémon names.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is open-source and available under the [MIT License](LICENSE).
