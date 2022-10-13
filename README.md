# Pool Ride

In day to day scenarios, it may be better to share your rides rather than take it entirely on your own for various reasons. With the removal of ride sharing options in major cab providers, there is no platform for commuters to pool their rides. We wish to address this pain point with an application.

## Solution
### Overview
Users provide their name, phone number, source and destination. They are matched with other users based on overlap of their routes. The users matched if:
- One route is contained in another
- The routes have overlap of more than 50%

The users are notified with the details of the ride partner and also the fare split among them is indicated. 

The application will be later updated to handle other cases of route matching and the respective fare sharing.
### Implementation details

- The user can input the source and destination by typing the address (auto suggestions are also provided) and book the ride.
- The corresponding geo coordinates are found and the route/path is saved as an encoded polyline, which is a compression algorithm that allows you to store a series of coordinates as a single string.
- Users are matched using the encoded polyline on the above mentioned criteria.
- The details of the other user are shared once matched.

### Tools & Technologies
- Flask
- HERE Maps

### Demo/Code
Link to demo video: https://drive.google.com/file/d/1E6otzde-yZA8M0vy2oFDHXKtAmM3qoHT/view?usp=drivesdk
