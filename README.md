# news-bulletin

[](/usage.png)

````
# news-bulletin

news-bulletin is a Python script that allows you to quickly access short news headlines and summaries directly from your command line interface (CLI). It fetches the latest news from various sources and presents them in a concise format, making it convenient for users to stay updated with the latest news without leaving the terminal.

## Features

- Fetches short news headlines and summaries from multiple sources.
- Supports customization of news sources and categories.
- Provides direct links to read full articles for each news item.

## Prerequisites

- Python 3.6 or above installed on your system.
- An internet connection to fetch the latest news data.

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Saif-Shines/news-bulletin.git
````

2. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

3. Run the script to start fetching news:

   ```shell
   python news_cli.py
   ```

## Usage

- Run the script with the command shown above to fetch and display the latest news.
- Use the arrow keys to navigate through the news items.
- Press `Enter` to open the full article in your default browser.
- Use the options and commands provided in the CLI menu to customize news sources and categories.

### `.env`

```sh
NEWS_API_KEY="api-key"
# from https://newsapi.org/docs/endpoints/everything
```

```sh
python3 news_cli.py "Your Query"
```

## Configuration

The script uses a configuration file (`config.json`) to manage news sources and categories. By default, it includes popular news sources and general news categories. You can modify this file to customize the sources and categories according to your preferences.

## Contributing

Contributions to news-bulletin are welcome! If you find any issues, have suggestions for improvements, or want to add new features, feel free to open an issue or submit a pull request. Please make sure to follow the code of conduct in all interactions.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

The script uses the [NewsAPI](https://newsapi.org/) service to fetch news data. Special thanks to the developers and contributors of the NewsAPI project.

```

```
