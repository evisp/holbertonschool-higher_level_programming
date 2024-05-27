# READ ME

## Task 5

### Testing with cURL Commands

#### 1. Accessing `/basic-protected` without credentials

```bash
curl -i http://localhost:5000/basic-protected
```

#### 2. Accessing `/basic-protected` with valid credentials:

```bash
curl -i -u user1:password http://localhost:5000/basic-protected
```

#### 3. Posting valid credentials to `/login`:

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"username": "user1", "password": "password"}' http://localhost:5000/login

```

#### 4. Accessing `/jwt-protected` without a token or with an invalid token

```bash
curl -i http://localhost:5000/jwt-protected
```

#### 5.  Accessing `/jwt-protected` with a valid token:

```bash
curl -i -H "Authorization: Bearer <JWT_TOKEN>" http://localhost:5000/jwt-protected
```

#### 5.  Accessing `/jwt-protected` with a valid token:

```bash
curl -i -H "Authorization: Bearer <JWT_TOKEN>" http://localhost:5000/jwt-protected
```

#### 6.  Accessing `/admin-only` with a non-admin token

```bash
curl -i -H "Authorization: Bearer <JWT_TOKEN>" http://localhost:5000/admin-only
```

#### 7.  Accessing `/admin-only` with an admin token

```bash
curl -i -H "Authorization: Bearer <ADMIN_JWT_TOKEN>" http://localhost:5000/admin-only
```
