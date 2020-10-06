people = {{people}}
environments = {{environments}}
people_names = [person['person']['name'] for person in people]
env_names = [env.lower() for env in list(environments)]
env_qtd = len(env_names)
new_env_probality = [float(100/env_qtd)]*env_qtd
