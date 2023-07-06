# Preprocessing of Stock Trades Data
This project focuses on preprocessing stock trades data extracted from a PDF document. The goal is to clean and structure the extracted data for further analysis and modeling.

## Libraries
The following library is used in this project:

tika: For extracting text from the PDF document.

## Input
The input for this preprocessing step is a PDF document containing stock trades data. The path to the PDF file is provided as input_pdf_path.

## Text Extraction
The PDF document is parsed using the tika library, which extracts the raw text from the document. The extracted text is split into individual lines for further processing.

## Data Cleaning
The lines containing stock trades are identified by a specific prefix, '1-BOVESPA'. These lines are extracted and stored in the trades list.

## Filtering Trades
Some lines within the trades list represent different types of trades that are not relevant for the analysis. These lines are filtered out, resulting in the op_opcoes list that contains only the trades of interest.

## Data Transformation
The op_opcoes list is converted into a pandas DataFrame (df_trades) for easier manipulation and analysis. The DataFrame is split into separate columns using space as the delimiter.

## Handling Missing Data
In some cases, the extracted lines may have missing columns due to inconsistent formatting in the PDF document. To handle this, the code attempts to extract the columns of interest and, if a column is missing, inserts a None value. The resulting DataFrame is stored in df_trades_limpo.

## Final Data Extraction
The relevant columns from df_trades_limpo are extracted and stored in the lista_tr list as tuples. Each tuple represents a single trade and contains the following information: stock exchange (bov), operation type (op), trade date (data), stock ticker (ticker), quantity (qtd), unit value (vu), and total value (total).

## Results
The lista_tr list contains the preprocessed stock trades data, ready for further analysis or modeling. You can use this data to gain insights and make informed decisions based on the extracted information.

Feel free to explore the provided code and modify it according to your specific needs. Use this preprocessing step as a foundation for analyzing stock trades data extracted from PDF documents!
