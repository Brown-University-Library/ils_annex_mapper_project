[![code-best-practices image](https://library.brown.edu/good_code/project_image/ils_annex_mapper/)](https://library.brown.edu/good_code/project_info/ils_annex_mapper/)


#### overview

This is the web-app code for an API that maps codes in our [Sierra ILS](https://www.iii.com/products/sierra-ils/) to codes for the [GFA](https://www.gfatech.com) Library Archival Systems (LAS) inventory-control software used by our offsite [Annex](https://library.brown.edu/about/annex/) storage facility.

Specifically, it maps Sierra `LOCATION` codes to GFA `CUSTOMER_CODE` codes, and Sierra `PICKUP AT` codes to GFA `DELIVERY STOP` codes.

It is used by one of the annex-processing services -- specifically, one which [processes emailed pageslips](https://github.com/Brown-University-Library/annex_process_email_pageslips) to extract data for the GFA LAS software.

- Usage examples:

    - `api-url/location_api_v2/ils_code_ANNEX/` returns data including results for the submitted code, like...

            {
              "request": {
                "requested_ils_code": "ANNEX"
              },
              "result": {
                "definition_ils_code": "Sierra \"LOCATION\" code",
                "definition_las_code": "LAS \"CUSTOMER_CODE\" code",
                "returned_las_code": "QS",
                "service_documentation": "https://github.com/birkin/ils_annex_mapper_project/blob/master/README.md"
              }
            }

    - `api-url/pickup_api_v2/ils_code_ANNEX/` returns data including results for the submitted code, like...

            {
              "request": {
                "requested_ils_code": "ANNEX"
              },
              "result": {
                "definition_ils_code": "Sierra \"PICKUP AT\" code",
                "definition_las_code": "LAS \"DELIVERY STOP\" code",
                "returned_las_code": "AN",
                "service_documentation": "https://github.com/birkin/ils_annex_mapper_project/blob/master/README.md"
              }
            }

    - `api-url/location_api_v1/all/` shows all of the location-mapping codes

    - `api-url/pickup_api_v1/all/` shows all of the pickup-mapping codes


- Permitted staff may edit entries via the url `api-url/admin/`.

- code contact: [birkin](mailto:birkin_diana@brown.edu)
