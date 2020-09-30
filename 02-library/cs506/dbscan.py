from .sim import euclidean_dist
class DBC(): 

	def __init__ (self, dataset, min_pts, epsilon):
		self.dataset = dataset
		self.min_pts = min_pts
		self.epsilon = epsilon
		
	def _get_neighborhood(self, P):
		Negihborhood = []
		for PN in range(len(self.dataset)):
			if euclidean_dist(self.dataset[P], self.dataset[PN]) <= self.epsilon:
				Neighborhood.append(PN)
		return Neighborhood
		
	def _explore_PNeighborhood(self, assignments, assignment, P, PNeighborhood):
		
		while PNeighborhood:
			NextP = Pneighborhood.pop()
			NextPNeighborhood = self._get_neighborhood(Pn)
			
			if assignments[NextP] == -1:
				assignments[NextP] = assignment
				
			if assignmennts[NextP] == 0: 
				
				if len(NextPNeighborhood) >= self.min_pts:
					PNeighborhood += NextPNeighborhood
		
				assignments[NextP] = assignment 
		
		return assignments
		
		
	def dbscan(self):
		assignments = [0 for _ in range(len(self.dataset))]
		assignment = 1
		
		for P in range(len(self.dataset)):
			if assignments[P] != 0:
				continue
			
			aassignment += 1
			PNeighborhood = self._get_neighborhood(P)
			if len(PNeighborhood) >= self.min_pts:
				# core point 
				assignments = self._explore_PNeighbrhood(assignments, assignment, P, PNeighborhood)
			else:
				# either border or noise 
				assignments[P] = -1
		
		return assignments