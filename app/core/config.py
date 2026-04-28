from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config =  SettingsConfigDict(env_file='.env')

    app_name: str
    app_version: str
    debug: bool
    host: str
    port: int
    database_url: str
    
    auth_username: str
    auth_password: str
    secret_key : str
    algorithm : str
    acces_token_expire_minutes : int
    


settings = Settings()



