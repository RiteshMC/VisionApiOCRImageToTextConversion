# Cloud Vision Api OCR ImageToTextConversion

# Overview

Using a pre-trained Vision API to detect text and then print it in the same format as the image as much as possible.
Basically converting a image such as invoices to text format

## System environment

Python Used : 3.9.2

## System Requirement

1. Cloud Vision Api Key
```
# Paste your api-key in main.py file
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

2. Image URL
```
# Prope image url or you can just use the following for test purposes
image_url = "https://raw.githubusercontent.com/RiteshMC/VisionApiOCRImageToTextConversion/main/resources/test-invoice.jpg"
```

## Procedure

Once you download the project and change the api-key, you can directly hit the script.
You will receive an output something similar to below or you can check the output.txt file attached.

Command : ```python main.py```

Image reference :  [Image Link](https://raw.githubusercontent.com/RiteshMC/VisionApiOCRImageToTextConversion/main/resources/test-invoice.jpg) 

Output
```
Total Sentences =  73
========================

"ABCTravel", "INVOICE"
"SMALLSYSINC"
"795EDRAGRAM"
"TUCSONAZ85705"
"USA", "LOGO"
"abc.travel"
"904041234"
"BILLTO", "SHIPTO", "InvoiceNo:#INV00001"
"BillyJean", "JohnTravis", "InvoiceDate:2020/11/11"
"DEFTravel", "GHJTravel", "DueDate:2020/12/12"
"904041234", "904041234"
"DESCRIPTION", "QTY", "UNITPRICE", "TOTAL"
"ItemName1", "2", "20.00", "40.00"
"ItemName2", "3", "40.00", "120.00"
"ItemName3", "4", "20.00", "80.00"
"ItemName4", "2", "50.00", "100.00"
"ItemName5", "1", "60.00", "60.00"
"ItemName6", "6", "20.00", "120.00"
"ItemName7", "1", "80.00", "80.00"
..............
..............
..............
```

