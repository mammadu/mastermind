# mastermind

## user stories

- ~~As a user, I should be able to select 4 values, between 0 and 7, and receive feedback on my guess~~
- ~~As a user, I expect my feedback to tell me how many numbers were correct, how many numbers were correct and in the right location, and how many were incorrect~~
- ~~As a user, I should be able to make a guess, see my guess and feedback history, and see my remaining attempt count~~
- ~~As a user I expect to have 10 attempts to guess the code~~
- ~~as a user, I should be able to quit the game without causing a crash~~
- ~~as a developer, I should be able to push modifications to the repository for mastermind and automatically have it tested~~
- ~~as a developer, I should be able to push modifications to the repository for mastermind and automatically have it linted~~

## notes

## questions

### answered

### unanswered

- in what ways can I implement metrics for this game?
    - what metrics would I even record? How would I save said metrics?
        - metrics to record
            - highest score
            - lifetime player attempts
            - lifetime wins
            - lifetime losses
            - average attempt per game
        - saving methods?

## todo

- change CSV logger so that it doesn't log test information
- fix DRY violations
    - there are multiple locations in the code where the same default values are defined
        - Defaults should be defined at the highest level and then sent down to the modules...
