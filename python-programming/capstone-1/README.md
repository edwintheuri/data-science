# Python Capstone-1 ( Nutritional Tracking App)

Repo for my capstone project

1. ## Project Description 


    - This program shows how python can be used as  a tool to transform raw data into meaningful insights that support better nutritional decisions on all levels

    -  The app stores Nutritional data in Foodbank table and user recordings in the User_log table

    - Finally it analyzes the data logged and provides feedback to the user based on a recommended international baseline for macros and micros nutrients,

2. ## Features in the app 

    - Logging user food data using natural language eg (food)
    - Returning nutritional data of the food eg ( zinc : 3.5 , calcium : 4.0)
    - Comparing the nutritional data with the recommended baseline
    - simple interactive ui

3. ## Problem it solves

    - Many people lack awareness about their daily nutrients intake (protein, iron, zinc and energy) .

        - This app is providing a way to check this nutrients
            - Track food intake
            - Estimate nutrients consumed 
            - compare against recommended daily values from [fda](https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels)
4. ## Tools
    - Python (Logic)
    - Streamlit(User Interface)
    - Sqlite (Database)
    - CSV (Data ingestion)
    - regex (Parsing user input )

5. ## How it works 
    **Gather data from data-sets**
            (Currently) manually creating the data-set (limited)



    **Data food bank**

           - Sqlite database stores the food items and their nutrients 

                - Database columns: 
                    -Protein
                    -Iron
                    -Zinc
                    -Energy

                code using db_access.execute(''')
    **Empty Store to append user inputs later**

            -This acts as a reservation for appending food
                (cleaned_Data = [] )

    **Storage variables**

            - This acts as a starting point of 0 , for calcuating sum and qty
                (eg: protein = 0)

    **User Input**

            - User enters food they ate: 
                (eg: 2 friedegg, brownbread)

            - The streamlit check if user has no input 

    **Parsing engine**

            - The system: 
                -splits input
                    (using regex , (r'(,|\band\b)', user_data) )  

                -extracts quantity and food name by grouping them using ()

                    (using regex , (r'(\d*\.?\d+)?s*(.*)', user_data))   



    **Food Mapping**  

            -  Foods are mapped to the Cache function

                    using food_id = food_cache.get(food)

    **Nutrients Calculation**

            - Food nutrients are multiplied by quantity and summed

                eg.( SELECT name, qty FROM food_bank WHERE id = ? , (food_id) 
                    )       
                    total protein += protein * qty

    **Evaluation**

            - Results are compared to FDA baseline dieatary values 

            eg protein 50g

    **Recommendation**

            - Update user based on their nutrients to show if they are within the baseline

6. ## Limitations 

            - Approximating portion size
                    -eg knowing what 1 pancake is how many grams 
            - limited food name exacting and fuzzy implementations 
                     -eg data-set had  many names in one code cell, names have 2 words ie white bread , manually added as whitebread
            - No history tracking 
                    -eg app to know what the user ate in their last interaction 
            - No personalization
                    - eg age , weight , height , activity level

7. ## Future improvements 

            - Add portion estimate intelligence
            - Add fuzzy matching ie mokimo to mukimo(in db)
            - Store user log for a more personalized feel 
            - personalize baselines based on age, gender, activity etc
            - improve on automating data-set values 

8. ## References 

            - [FDA] food & drug administration US (https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels)
            - [Nipfn] National Information Platform for food Security and Nutrition (https://nipfn.knbs.or.ke/download/kenya-food-composition-tables-2018/)
        
         


            