import uvicorn

# Change uvicorn log messages so it shows filename and line no
log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(levelname)s: - %(message)s (%(filename)s:%(lineno)d)"
log_config["formatters"]["default"]["fmt"] = "%(levelname)s: - %(message)s (%(filename)s:%(lineno)d)"
