# Testing

Once the portal was operational I set about testing it for errors and to ensure any possible errors that can be made were caught.

The deployed project live link is [HERE](https://organized-life-a4f96feabeb5.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 


The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Instructions | User is given typed out instructions | Intro screen presented | Works as expected |
| Name input | User is asked to enter their name | First & Last name input| Works as expected | 
| Name input | User inputs symbol or number | Error message appears | Works as expected | 
| Profession | User selects their profession | User selects a - f | Works as expected | 
| Profession | User selects invalid letter | Error message appears | Works as expected | 
| Information | User given contractor No & pay | Information confirmed as true | Works as expected |
| Information | Information entered incorrect | Notice appears to start again | Works as expected |
| Dates & hours | User adds dates, days and hours | Correct information confirmed | Works as expected |
| Dates & hours | Incorrect information added | Error message appears | Works as expected |
| "n" option  | User selects no to confirmation | Notice appears to start again | Works as expected |
| Confirmed Info | Everything entered presented | Pay amount minus tax & NI appears | Works as expected |
| Submit info | Everything entered ready to submit | Users clicks y to submit | Works as expected |
| Submit info | Ready to submit, n selected | Notice appears to start again | Works as expected |

## Testing Browsers
The portal was tested in the following browsers (based on my own testing and those of people who tested the portal):

- Chrome
- Oprea

It worked without issues in the above browsers.


## Validation

### PEP8 validator 

* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code. The results show that there is trailing whitespace. The reason why I added trailing whitespaces from line 11 to line 30 was because it was neccessary to have it to accomplish my formatting of the ''Organize life'' ascci art.
Other than that, no errors were found.

![x](documentation/images/pep8.png)





*<span style="color: blue;">[Back to Content](#content)</span>*
