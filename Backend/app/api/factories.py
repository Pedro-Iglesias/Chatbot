

from Backend.app.application.login_admin import LoginAdmin
from Backend.app.application.delete_document import DeleteDocument
from Backend.app.application.list_documents import ListDocuments
from Backend.app.application.create_document import CreateDocument
from Backend.app.application.update_document import UpdateDocument
from Backend.app.application.create_user import CreateUser
from Backend.app.application.list_users import ListUsers
from Backend.app.application.update_user import UpdateUser
from Backend.app.application.delete_user import DeleteUser
from Backend.app.infrastructure.repositories.sql.postgres_document_repository import (
    PostgresDocumentRepository,
)
from Backend.app.infrastructure.repositories.sql.postgres_user_repository import (
    PostgresUserRepository,
)


class AuthFactory:
    @staticmethod
    def make_login() -> LoginAdmin:
        return LoginAdmin()


class DocumentFactory:
    @staticmethod
    def make_delete() -> DeleteDocument:
        repository = PostgresDocumentRepository()
        return DeleteDocument(repository=repository)

    @staticmethod
    def make_list() -> ListDocuments:
        return ListDocuments()

    @staticmethod
    def make_create() -> CreateDocument:
        repository = PostgresDocumentRepository()
        return CreateDocument(repository=repository)

    @staticmethod
    def make_update() -> UpdateDocument:
        repository = PostgresDocumentRepository()
        return UpdateDocument(repository=repository)


class UserFactory:
    @staticmethod
    def make_create() -> CreateUser:
        repository = PostgresUserRepository()
        return CreateUser(repository=repository)

    @staticmethod
    def make_list() -> ListUsers:
        repository = PostgresUserRepository()
        return ListUsers(repository=repository)

    @staticmethod
    def make_update() -> UpdateUser:
        repository = PostgresUserRepository()
        return UpdateUser(repository=repository)

    @staticmethod
    def make_delete() -> DeleteUser:
        repository = PostgresUserRepository()
        return DeleteUser(repository=repository)