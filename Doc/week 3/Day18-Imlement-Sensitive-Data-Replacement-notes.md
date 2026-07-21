Today, I'm going to replace sensitive data with protected data (using Dummy Data).

I just created dummy data and placed it in the backend folder in the application section, in the mocking subsection. The data contains two sets of dummy data: entities and text. I also created a pseudonymization_service to use the dummy data from the mock, by importing dumydata_entities.py and dumydata_text. Then, I used redact_service.py to update it using only the dummy data. If you want to see proof, you can access the image folder for Entities or Text.
