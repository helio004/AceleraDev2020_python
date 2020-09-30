# Import of methods that is importants 
from collections import Counter


from rest_framework.decorators import api_view
from rest_framework.response import Response

# insert of decorator method
@api_view(["POST"])
def lambda_function(request):
    if request.method == "POST": # verifying if the method is POST
        data = request.data.get('question') # create data for using in number generation in Solution
        solution = [s for i, n in Counter(data).most_common() for s in [i]*n] # create solution with list comprehension

    return Response({'solution': solution}) # Return a dictionary on the results of request
