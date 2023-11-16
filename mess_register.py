import requests

endpoint = 'https://sva.iith.ac.in/api/student/register'
# token = 'BEARER eyJhbGciOiJSUzI1NiIsImtpZCI6ImQwNWI0MDljNmYyMmM0MDNlMWY5MWY5ODY3YWM0OTJhOTA2MTk1NTgiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkFOR0EgQVJBVklORCBTSE9VTklLIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBVFhBSnh3OUJJSk94M3hFcDdlbU96UVdjMXZObDNUSWdOdjExd3VRXzF5PXM5Ni1jIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3N2YS1paXRoLWM0ZWMzIiwiYXVkIjoic3ZhLWlpdGgtYzRlYzMiLCJhdXRoX3RpbWUiOjE2NzUxNzE3NjQsInVzZXJfaWQiOiI0WnZKRnJOUFd3TlBTNXNRSHhIa0lwMHFzc00yIiwic3ViIjoiNFp2SkZyTlBXd05QUzVzUUh4SGtJcDBxc3NNMiIsImlhdCI6MTY3NTE3MTc2NCwiZXhwIjoxNjc1MTc1MzY0LCJlbWFpbCI6ImNzMjBidGVjaDExMDU1QGlpdGguYWMuaW4iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDEzMjYzODQyMDM4MDc1OTM5MyJdLCJlbWFpbCI6WyJjczIwYnRlY2gxMTA1NUBpaXRoLmFjLmluIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.LbzFJo-SNwlyWuVx1l50U1D9vsox64HHB-zJpbJqBFt_OvLSClCELSJ_iIiXiGmLf0Mb5CztYW19RA0UDFlKcZjBMKeVdmOFHf_KCubWlBaHgV0JYF_JldYmolifbgXEeluBvB7pnLW9vyMsChCr8NpFj4QMgEpVVEanJCP5SMGGIjm4eCJ_WAmTrzcIp-dv1vouOZcqVlY9u_n_BN_zJr07PpGY7A2iM29092uhB8JjkCF2zOXnDbjsHwI4bIT4EuS98l8gydgsHbZfUZXDqHldKJwImFKRNKOzA1VwTerlb3U0b7VdXKAMyOQJFVteSmq5D4YCb24MZzarDfVH9A'
# token = 'BBEARER eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk3OWVkMTU1OTdhYjM1Zjc4MjljZTc0NDMwN2I3OTNiN2ViZWIyZjAiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkFOR0EgQVJBVklORCBTSE9VTklLIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBVFhBSnh3OUJJSk94M3hFcDdlbU96UVdjMXZObDNUSWdOdjExd3VRXzF5PXM5Ni1jIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3N2YS1paXRoLWM0ZWMzIiwiYXVkIjoic3ZhLWlpdGgtYzRlYzMiLCJhdXRoX3RpbWUiOjE2ODAyNzA1MTQsInVzZXJfaWQiOiI0WnZKRnJOUFd3TlBTNXNRSHhIa0lwMHFzc00yIiwic3ViIjoiNFp2SkZyTlBXd05QUzVzUUh4SGtJcDBxc3NNMiIsImlhdCI6MTY4MDI3NDc1NCwiZXhwIjoxNjgwMjc4MzU0LCJlbWFpbCI6ImNzMjBidGVjaDExMDU1QGlpdGguYWMuaW4iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDEzMjYzODQyMDM4MDc1OTM5MyJdLCJlbWFpbCI6WyJjczIwYnRlY2gxMTA1NUBpaXRoLmFjLmluIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.S-5100XLJQ3BfqjdMMVJNM53aTBmiDXYMKOn7EWjn4aDXwPQikTql29VEukhTgjT2d3njxEs_Nq8CMaynBzyDDElMXtsg2Fh2OD8Nb3DhtIbLgt1s7TNZ89Wy1zRaqmO_YU3w32cMkgFhh30ggzzumbc2rKWHsTAn4v7a5yoC85mrX63u9XVt2LOxuKIAJx7JCow8eXCuxQiY4w9iq46YPjpBlVHAvjs4kuzApAQljjtg9TORzJta-hKX2J0590f6xy8b9a_xDolA5Fk45pjbBJiI3XoxagNPhlJQKdQhkejT89UedQ_Vx0NWKN0zzHqS2is1Xsmz2DdUQUHtIXCow'

token = 'BEARER eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk3OWVkMTU1OTdhYjM1Zjc4MjljZTc0NDMwN2I3OTNiN2ViZWIyZjAiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkFOR0EgQVJBVklORCBTSE9VTklLIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBVFhBSnh3OUJJSk94M3hFcDdlbU96UVdjMXZObDNUSWdOdjExd3VRXzF5PXM5Ni1jIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3N2YS1paXRoLWM0ZWMzIiwiYXVkIjoic3ZhLWlpdGgtYzRlYzMiLCJhdXRoX3RpbWUiOjE2ODAyNzA1MTQsInVzZXJfaWQiOiI0WnZKRnJOUFd3TlBTNXNRSHhIa0lwMHFzc00yIiwic3ViIjoiNFp2SkZyTlBXd05QUzVzUUh4SGtJcDBxc3NNMiIsImlhdCI6MTY4MDI3NDc1NCwiZXhwIjoxNjgwMjc4MzU0LCJlbWFpbCI6ImNzMjBidGVjaDExMDU1QGlpdGguYWMuaW4iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDEzMjYzODQyMDM4MDc1OTM5MyJdLCJlbWFpbCI6WyJjczIwYnRlY2gxMTA1NUBpaXRoLmFjLmluIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.S-5100XLJQ3BfqjdMMVJNM53aTBmiDXYMKOn7EWjn4aDXwPQikTql29VEukhTgjT2d3njxEs_Nq8CMaynBzyDDElMXtsg2Fh2OD8Nb3DhtIbLgt1s7TNZ89Wy1zRaqmO_YU3w32cMkgFhh30ggzzumbc2rKWHsTAn4v7a5yoC85mrX63u9XVt2LOxuKIAJx7JCow8eXCuxQiY4w9iq46YPjpBlVHAvjs4kuzApAQljjtg9TORzJta-hKX2J0590f6xy8b9a_xDolA5Fk45pjbBJiI3XoxagNPhlJQKdQhkejT89UedQ_Vx0NWKN0zzHqS2is1Xsmz2DdUQUHtIXCow'

dining_hall = 'UDH'

response = requests.post(endpoint,
    headers={'Authorization' : token}, 
    data={'name' : dining_hall}
    ).json()

print(response['message'])