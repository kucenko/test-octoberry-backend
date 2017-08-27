case "$ENVIRONMENT" in
    "production")
        export DATABASE_HOST='db'
        export DATABASE_PORT=5432
        export DATABASE_NAME='octoberry_production'
        export DATABASE_USERNAME='octoberry'
        export DATABASE_PASSWORD='octoberry'
        ;;
    *)
        export DATABASE_HOST='localhost'
        export DATABASE_PORT=5432
        export DATABASE_NAME='octoberry_development'
        export DATABASE_USERNAME='octoberry'
        export DATABASE_PASSWORD='octoberry'
        ;;
esac
