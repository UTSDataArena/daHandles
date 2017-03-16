request_dependency(cyclops)
request_dependency(daInput)
install(DIRECTORY . DESTINATION omegalib/modules/daHandles PATTERN ".git" EXCLUDE)
