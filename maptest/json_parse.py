import json

json_str = '''
{
                "vertexcnt":"98",
                "vertex":
                [
                    {
                        "x":127.10807,
                        "y":37.512062
                    },
                    {
                        "x":127.107872,
                        "y":37.512554
                    },
                    {
                        "x":127.107872,
                        "y":37.512554
                    },
                    {
                        "x":127.107689,
                        "y":37.512981
                    },
                    {
                        "x":127.107689,
                        "y":37.512981
                    },
                    {
                        "x":127.107475,
                        "y":37.513466
                    },
                    {
                        "x":127.107475,
                        "y":37.513466
                    },
                    {
                        "x":127.107399,
                        "y":37.513649
                    },
                   
                ],
           }
'''
dump = json.dumps(json_str)
data = json.loads(dump)

print(data['vertexcnt'])