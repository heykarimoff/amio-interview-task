# Maze python-code
Example application code for the [Senior Developer - homework](https://docs.google.com/document/d/1ns5vAOxMHLcuoxvqSIRq3WzM4PFYPCe65UUOhHI3flw/edit).

Deployed on Heroku at [https://mazeapi.herokuapp.com](https://mazeapi.herokuapp.com/).
Visit [API documentation](https://documenter.getpostman.com/view/14594760/UVXonEUP) to see available endpoints.
### Installation
Install dependencies:
```sh
pip install -r requirements.txt
```

### Usage
#### Start server
```sh
make up
```
#### Create Maze
```sh
curl --request POST 'localhost:5005/v1/mazes' --header 'Content-Type: application/json' --data-raw '[3, 1, [2, [5,[4, 3]]], [], [2]]'
{
  "content": [
    3, 
    1, 
    [
      2, 
      [
        5, 
        [
          4, 
          3
        ]
      ]
    ], 
    [], 
    [
      2
    ]
  ], 
  "id": 244273
}
```
#### Search Values in Maze
```sh
curl --request GET 'localhost:5005/v1/mazes/244273/values?value=2&operator=greater_than_or_equal'                                    
[
  3, 
  2, 
  5, 
  4, 
  3, 
  2
]

```