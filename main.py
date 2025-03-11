from MealIdeaGenerator import MealIdeaGenerator
import zmq

def main():
    context = zmq.Context()
    
    # Create reply socket
    socket = context.socket(zmq.REP)
    socket.bind("tcp://localhost:5557")
    
    while True:
        # Receive message (string of food items separated by commas)
        listAsString = socket.recv().decode()
        listAsList = listAsString.split(",")
        
        # Strip all elements of list
        listAsList = [item.strip() for item in listAsList]
        
        # Create idea generator
        ideaGen = MealIdeaGenerator()
        
        # Get possible meals
        possibleMeals = ideaGen.getIdeasFromFood(listAsList)
        
        # Send back possible meals as a string
        socket.send_string(", ".join(possibleMeals))
        
main()