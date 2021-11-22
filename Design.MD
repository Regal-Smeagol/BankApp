## Architecture
    * Encapsulation is paramount. Everything needs to be separated
    * 3-tier design
    * API handles user data IO
    * Service Layer handles the logic and input validation if necessary
    * Data Access Layer handles all database interactions
    * User authorization is not required
    * Employee class is not required
    
# Classes
    * API
        - Webpage
        - User experience
        - Use postman to test
    * Service Layer
        - Needs to have data structures to represent all data
        - Structures:
            = System/Bank
                > reject invalid transactions
            = Customer
                > can create accounts
                > can close accounts
                > witdraw/deposit
                > transfer
                    < by account ID
                > update personal info
                > can end business relationship
            = Account