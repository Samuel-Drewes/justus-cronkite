# Lebanon Climate Change Analysis

A Streamlit web application for analyzing climate change data in Lebanon.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- uv package manager (recommended) or pip

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd lebanon_climate_change
   ```

2. **Install dependencies using uv (recommended):**
   ```bash
   uv pip install -r requirements.txt
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:8501
   ```

## 📁 Project Structure

```
lebanon_climate_change/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── .gitignore                     # Git ignore patterns
├── README.md                      # This file
├── 41477_2022_1339_MOESM2_ESM.xlsx  # Data file
└── Untitled.ipynb               # Jupyter notebook
```

## 🔧 Features

- **Overview**: Project summary and key metrics
- **Data Analysis**: Upload and analyze climate data files
- **Visualizations**: Interactive charts and graphs
- **Insights**: Key findings and recommendations

## 📊 Data Sources

The application supports:
- Excel files (.xlsx)
- CSV files (.csv)
- JSON files (.json)

## 🎨 Configuration

The app is configured via `.streamlit/config.toml`:
- Custom theme colors
- Server settings
- Upload limits
- Browser preferences

## 🛠️ Development

### Adding New Features

1. Create new functions in `app.py`
2. Add navigation options in the sidebar
3. Update requirements if new packages are needed

### Customization

- **Theme**: Edit `.streamlit/config.toml` to change colors and styling
- **Data Processing**: Modify functions in `app.py` for your specific data format
- **Visualizations**: Add new chart types using Plotly or other visualization libraries

## 📦 Dependencies

- **streamlit**: Web app framework
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **plotly**: Interactive visualizations
- **openpyxl**: Excel file support
- **python-dotenv**: Environment variable management
- **joblib**: Caching and parallel processing

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   streamlit run app.py --server.port 8502
   ```

2. **Module not found:**
   ```bash
   uv pip install -r requirements.txt
   ```

3. **File upload issues:**
   - Check file format (xlsx, csv, json)
   - Ensure file size is under 200MB

### Getting Help

- Check the Streamlit [documentation](https://docs.streamlit.io/)
- Review error messages in the browser console
- Ensure all dependencies are installed correctly

## 📝 License

This project is for educational and research purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Submit a pull request

---

**Happy analyzing! 🌍📊**
