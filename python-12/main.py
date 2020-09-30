
doc = '''
#%RAML 1.0
title: challangeapi
version: 0.1v
mediaType: application/json
baseUri: http://localhost/codenationapi
securitySchemes:
    JWT:
      description: for token autentication with Token Jet.
      type: JWT
      describedBy:
        headers:
          Authorization: 
            description: User for post JSON Web Token no request
            type: string
            required: true
        responses:
          401:
            description: |
              invalid Token or expired. Please, try again.
      settings:
        signatures: ['HMAC-SHA256'] 
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: 
        type: string
        required: true
  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id:
        required: true
        type: integer
      user_id:
        required: true
        type: integer
      name: 
        type: string
        maxLength: 50
      status: boolean
      evironment: 
        type: string
        maxLength: 50
      version: string
      address: 
        type: string
        maxLength: 39
    example:
      agent_id: 2
      user_id: 4
      name: test
      status: true
      evironment: test
      version: 0.1v
      address: challengeapi.net
  Event:
    type: object
    discriminator: event_id
    properties:
      event_id: 
        type: integer
        required: true
      agent_id: 
        type: integer
      level: 
        type: string
        maxLength: 20
      payload: 
        type: string
      shelved: 
        type: boolean
      data: 
        type: date-only
    example:
      agent_id: 1
      event_id: 0
      data: 2020-07-01
      level: good
      payload: test
      shelve: true
  Group:
    type: object
    discriminator: group_id
    properties:
      group_id:
        type: integer
        format: int64
      name: 
        type: string
        maxLegth: 20
    example:
      group_id: 2
      name: namegroup
  User:
    type: object
    discriminator: user_id
    properties:
      user_id: 
        type: integer
        required: true
      name:
        type: string
        maxLength: 50
      password:
        type: string
        maxLength: 50
      email: 
        type: string
        maxLength: 254
      last_login: date-only
    example:
      user_id: 1
      name: yourname
      password: yourpassword
      email: youremail@email.com
      last_login: 2020-01-01

/auth/token:
  description: getting the token of authentication.
  post:
    body:
      application/json:
        properties:
          name: string
          password: string

    responses:
      201:
        body:
          application/json:
            type: Auth
      400:
        body:
          application/json:
            example:
              {"error": "Authentication Error"}
/agents:
  post:
    description: add new agent.
    securedBy: JWT
    body:
      application/json:
        properties:
          example: |
            {"agent_id": 1,
            "name": "teste",
            "status": true,
            "environment": "teste",
            "version": "0.1v",
            "address": "api.com",
            "user_id": 1}
    responses:
      201:
        body:
          application/json:
            exemple: 
              Agent
      401:
        body:
          application/json:
            example: |
              {"error": "permission denied"}
  
  get:
    description: return all agents.
    securedBy: JWT
    responses:
      200:
        body:
          application/json:
            default: Agent[]
  /{id}:
    get:
      description: Return a user with specific id.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    put:
      description: update for agent by the id.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad request"}
    delete:
      description: delete agent by the id.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
  /{id}/events:
    post:
      description: adds more one event in the agent.
      securedBy: JWT
      body:
        application/json: 
          Event
        201:
          body:
            application/json: |
              {"message": "Created"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
      responses:
        201:
          body:
            application/json:
              Event
        401:
          body:
            application/json:
              {"error": "permission denied"}
    get:
      description: Return all events of a agent.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Event[]
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    put:
      description: change events of a agent.
      securedBy: JWT
      body:
        application/json: Event
        200:
          body:
            application/json: 
              exemplo:
                {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
      responses: 
        200:
          body:
            application/json:
              exemplo:
                {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
    delete:
      description: removing one or more events of a agent.
      securedBy: [JWT]
      body:
        application/json:
          Event
        200:
          body:
            application/json: 
              exemplo:
                {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
      responses:
        200:
          body:
            application/json: 
              exemplo:
                {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
  /{id}/events/{id}:
    get:
      description: return event with specific id.
      securedBy: JWT
      body:
        application/json:
      responses:
        200:
          body:
            application/json: 
              exemplo:
                {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    put:
      description: update event by the id.
      securedBy: JWT
      body: 
        application/json: Event[]
      responses:
        200:
          body:
            application/json: 
              exemplo:
                {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    delete:
      description: remove agent by the id.
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
        401:
          body:
            application/json:
        404:
          body:
            application/json:
/users:
  post:
    description: add new user.
    securedBy: JWT
    body:
      application/json:
        properties:
          name: 
            type: string
            maxLength: 50
          password:
            type: string
            maxLength: 50
          email: 
            type: string
            maxLength: 254
          last_date: date-only
        example: |
          {"name": "Username",
          "email": "email@email.com",
          "password": "yourpassword",
          "last_login": "2020-07-02"}
    responses:
      201:
          body:
            application/json: |
              {"message": "Created"}
      401:
        body:
          application/json: |
            {"error": "permission denied"}
  get:
    description: return all users.
    securedBy: JWT
    responses:
      200:
        body: 
          application/json: User[]
      401:
        body:
          application/json: |
            {"error": "permission denied"}

  /{id}:
    get:
      description: search a specific user by the id.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: User
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    put:
      description: changing a specific user.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    delete:
      description: remove a specific user by the id.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
/groups:
  post:
    description: add new group.
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 20
        example: |
          {"name": "group_name"}
    responses:
      201:
        body:
          application/json: |
            {"message": "Ok"}
      401:
        body:
            application/json: |
              {"error": "permission denied"}
  get:
    description: return all groups.
    securedBy: JWT
    responses:
      200:
        body:
          application/json: Group[]
      401:
        body:
            application/json: |
              {"error": "permission denied"}
      404:
        body:
          application/json:
  put:
    description: Change a group.
    responses:
      200:
        body:
          application/json:
  delete:
    description: Delete a group.
    responses:
      200:
        body:
          application/json:
  /{id}:
    get:
      description: search a group.
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Group
        401:
          body:
            application/json:
        404:
          body:
            application/json:
    put:
      description: changing a group.
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
        401:
          body:
            application/json: |
              {"error": "permission denied"}
    delete:
      description: remove a group.
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
        401:
          body:
            application/json: |
              {"error": "permission denied"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
'''
