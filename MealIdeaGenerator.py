import os
from constraint import *

class MealIdeaGenerator:
    def __init__(self):
        self.recipeDirectoryPath = "C:\\Users\\hyper\\OneDrive\\Documents\\Classes\\2025Winter\\SoE\\RecipeStorage\\recipes"
        
        self.recipeNameToIngredientsDict = {}
        # Iterate through all recipe files
        for fileName in os.listdir(self.recipeDirectoryPath):
            # Open the current file
            with open(self.recipeDirectoryPath + "\\" + fileName, "r") as currFile:
                currentRecipeIngredients = []
                
                # Get all ingredients in the current recipe
                for line in currFile.readlines():
                    if line != "" and line != "\n":
                        currentRecipeIngredients.append(line.strip().lower())
                        
                # Add the current recipe and its list of ingredients to the dict
                self.recipeNameToIngredientsDict[fileName[:-4].lower()] = currentRecipeIngredients # index :-4 removes the .txt extension              
    
    def getIdeasFromFood(self, foodList):
        ideas = []
        
        # Iterate through dict
        for recipeName in self.recipeNameToIngredientsDict:
            # Check if the current recipe is a subset of the available food
            if set(self.recipeNameToIngredientsDict[recipeName]) <= set(foodList):
                ideas.append(recipeName)
                
        return ideas
        
        
    
ideaGen = MealIdeaGenerator()
ideaGen.getIdeasFromFood(["tortilla", "cheese"])