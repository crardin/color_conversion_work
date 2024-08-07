function [Vertices Edges Faces VertexCoefficients, FigureHandle] = ...
		        ConstructPositiveZonohedron(GeneratingVectors)
% Purpose		Find the vertices, edges, and faces of the zonohedron generated by a set of
%				three-dimensional vectors, all of whose entries are non-negative.  The
%				generating vectors must be in general position: no input 
%				vector can be identically 0, no two input vectors can be parallel, and no
%				three input vectors can be linearly dependent.
%
% Description	A zonohedron is the set of all linear combinations of a set of generating
%				vectors, such that the coefficients of any linear combination is between
%				0 and 1, inclusive.  A zonohedron is a convex polytope.  Each edge of the
%				zonohedron is a translation of one of the generating vectors.  Each face 
%				of the zonohedron is a parallelogram.  The coefficients of the linear
%				combinations that make up the vertices are all either 0 or 1.  
%
%				This routine calculates the vertices, edges, and faces, of the zonohedron
%				generated by an input set of three-dimensional vectors.  It is assumed
%				that the vectors are all in the positive octant, so that all vector
%				coordinates are non-negative.  Furthermore, it is assumed that no two of
%				the input vectors are parallel, and no three are linearly dependent.  A
%				flag can be set internally to plot a figure of the zonohedron.
%
%				The algorithm uses the convexity of the zonohedron, and the fact that the
%				coefficients of all vertices are either 0 or 1.  The set of ALL linear
%				combinations of generating vectors, whose coefficients are either 0 or 1,
%				is called the set of nodes.  Some nodes can be inside the zonohedron, while
%				others are on the boundary.  All the nodes are calculated, and the function
%				convhulln determines which are on the boundary.  
%
%				Once the vertices are determined, the algorithm uses the fact that any
%				two adjacent vertices must differ by a generating vector.  All possible
%				pairs of vertices are checked, to see which ones satisfy this condition.
%				The result is a set of edges.
%
%				Finally, each face of a general-position zonohedron (i.e. one in which no
%				three generating vectors are linearly dependent) is a parallelogram.  This
%				fact is used, and pairs of parallel edges are checked, to see if they are
%				joined by another pair of parallel edges.  When they are, there is a face.
%
%				This function could likely be considerably generalized, without too much
%				trouble.  The restriction to the positive octant was made because the
%				motivating example was the display gamut of a set of monitor primaries in
%				CIE XYZ space, where all entries are non-negative.  Zonohedra can be
%				constructed for generating vectors in multiple octants simultaneously, 
%				which would be a natural generalization.  Similarly, general zonotopes,
%				where the generating vectors are in n-dimensional space, for n > 3, could
%				also be considered.  Even if the generating vectors are not in general
%				position, a zonohedron can still be constructed, so this case could be
%				considered, too.  
%
%				Finally, the algorithm used here involves brute force, and clarity
%				was chosen over optimization.  A more sophisticated algorithm, that 
%				would be faster and more efficient, would use the structure of zonohedra.
%				The zonohedron could be built up, generator by generator.  Say a zonohedron
%				for the first n-1 generators had been constructed.  The nth generator could
%				be added to the current zonohedron by inserting a new zone of parallelograms,
%				which all had two sides consisting of the nth generator.  The zone would be
%				inserted along the shadow boundary for the current zonohedron, in the direction
%				of the nth generator.  Continue until all generators have been inserted.
%				[Heckbert1985] suggests a similar algorithm.
%
%				References
%				[Heckbert1985] Paul Heckbert, An Efficient Algorithm for Generating
%								Zonohedra, 3-D Technical Memo 11, Computer Graphics Lab,
%								New York Institute of Technology, February 1985.
%
%				GeneratingVectors	A set of three-dimensional vectors in the positive octant.  The
%									zero vector is not allowed, and no two vectors may be parallel.
%
%				Vertices			A three-column matrix.  Each row gives the three-dimensional
%									coordinates of a vertex of the generated zonohedron.
%
%				Edges				A two-column matrix.  Each row gives an edge of the generated
%									zonohedron.  The entries of the matrix refer to the rows of the
%									Vertices matrix.  For example, the row [5,7] in the Edges matrix
%									means that the zonohedron contains an edge between the 5th and
%									7th rows (each of which is the three-dimensional coordinates of
%									a vertex) in the Vertices matrix.
%
%				Faces				A four-column matrix.  Each row gives a face of the generated
%									zonohedron.  The entries of the matrix refer to the rows of the
%									Vertices matrix.  For example, the row [5,7,3,2] in the Edges 
%									matrix means that the zonohedron contains a face whose vertices
%									are the 5th, 7th, 3rd, and 2nd rows of the Vertices matrix.  The
%									vertices are listed in either clockwise or counterclockwise
%									order, for easy plotting.  
%
%				VertexCoefficients	Each vertex is a linear combination of the generating vectors.
%									The ith row of the matrix VertexCoefficients gives the
%									coefficients of the generating vectors for the ith vertex, which
%									is given in the ith row of the matrix Vertices.
%
%				FigureHandle		Return a handle to the figure produced, for further modification
%									and saving
%
% Author		Paul Centore (March 30, 2014)
% Revision		Paul Centore (Dec. 29, 2015)
%				-----Eliminated duplicate faces
% Revision		Paul Centore (July 4, 2016)
%				-----Added figure handle as return variable
%
% Copyright 2014-2016 Paul Centore
%
%    This file is part of MunsellAndKubelkaMunkToolbox.
%
%    MunsellAndKubelkaMunkToolbox is free software: you can redistribute it and/or modify
%    it under the terms of the GNU General Public License as published by
%    the Free Software Foundation, either version 3 of the License, or
%    (at your option) any later version.
%
%    MunsellAndKubelkaMunkToolbox is distributed in the hope that it will be useful,
%    but WITHOUT ANY WARRANTY; without even the implied warranty of
%    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%    GNU General Public License for more details.
%
%    You should have received a copy of the GNU General Public License
%    along with MunsellAndKubelkaMunkToolbox.  If not, see <http://www.gnu.org/licenses/>.

DisplayFigure = true	;	% A flag for drawing a figure of the zonohedron

% Generate the nodes of the zonohedron.  A node is the sum of a subset of the generating
% vectors.  If the zonohedron is viewed as the set of linear combinations of the generating
% vectors, then a node is a linear combination for which every coefficient is either 0 or 1.
% Some nodes will be on the boundary of the zonohedron, while others will be inside.
NumberOfGeneratingVectors = size(GeneratingVectors,1)		;
CoefficientsOfNodes = powerset(1:NumberOfGeneratingVectors)	;
NumberOfNodes       = size(CoefficientsOfNodes,2)			;
CoordinatesOfNodes  = -99 * ones(NumberOfNodes,3)			;
for ctr = 1:NumberOfNodes
	ElementsInSubset = CoefficientsOfNodes{1,ctr}	;
	if isempty(ElementsInSubset)
		CoordinatesOfNodes(ctr,:) = [0 0 0] 		;
	else
		CoordinatesOfNodes(ctr,:) = [0 0 0]			;
		for idx = 1:length(ElementsInSubset)
			CoordinatesOfNodes(ctr,:) = CoordinatesOfNodes(ctr,:) + GeneratingVectors(ElementsInSubset(idx),:)	;
		end
	end
end

% Construct matrix with coefficients of nodes.  This matrix has one row for each node, and
% one column for each generating vector.  The entry in row i and column j  is 1 if the jth
% generating vector is used in the ith node, and 0 otherwise.
NodeCoefficients = zeros(NumberOfNodes,3)		;
for ctr = 1:NumberOfNodes
	NodeCoefficients(ctr,CoefficientsOfNodes{1,ctr}) = 1	;
end

% Some of the nodes are on the boundary of the zonohedron, while others are inside.  Since
% a zonohedron is convex, a node is on the boundary if it is contained in the convex hull
% of the set of nodes.  The function convhulln returns a matrix, each row of which contains
% the indices of the vertices of an (n-1)-dimensional face of the convex hull.  Any entry
% in this matrix (and only the entries in this matrix) are therefore the indices of
% boundary vertices.  (The index i in this case refers to the point given by the ith row
% of the matrix CoordinatesOfNodes.)  
TriangularFaces = convhulln(CoordinatesOfNodes)				;
VertexIndices   = unique(reshape(TriangularFaces,[],1))		;

% Extract coordinates for the vertices, and extract their coefficients as nodes
Vertices           = CoordinatesOfNodes(VertexIndices,:);
VertexCoefficients = NodeCoefficients(VertexIndices,:)	;
NumberOfVertices   = size(Vertices,1) 					;

% Find all the zonohedron s edges.  Two vertices of a zonohedron are joined by an edge if
% their difference is one of the generating vectors.  Search all pairs of vertices, to see
% which pairs satisfy this condition.  Create a two-column matrix, that contains one row
% for each edge.  Order the vertices of each edge, so that the one nearer the origin is
% first.
Edges 			  = [] 	;
DifferenceVectors = []	;
for ctr1 = 1:NumberOfVertices
	for ctr2 = setdiff(1:NumberOfVertices, ctr1)
		% The potential edge is the vector difference of two vertices.  
		VectorDiff = VertexCoefficients(ctr2,:) - VertexCoefficients(ctr1,:) ;	
		% The two vertices share an edge if and only if their vector difference is a
		% generating vector.  The difference is a generating vector if all its entries
		% are 0, except one entry, which is 1.  (We require an edge to be ordered, so
		% that the second vertex is the first vertex plus---not minus---a generating
		% vector.
		if isequal(sort(VectorDiff), [zeros(1,NumberOfGeneratingVectors-1), 1])
			Edges = [Edges; ctr1 ctr2] 	;
			% The edge is a translation of one of the generating vectors.  Find and
			% record which one.
			DifferenceVectors = [DifferenceVectors; find(VectorDiff == 1)]	;
		end
	end
end

% There is one zone for each generating vector.  That zone consists of all the edges that
% are translations of that generating vector, and all the parallelograms which have two
% sides that are translations of that vector.  The variable DifferenceVectors already 
% records which generating vector each edge is a translation of.  A zone for a particular
% generating vector can therefore be found by extracting all the edges whose corresponding
% difference vector is that generating vector.  
Faces = []	;
for ctr = 1:NumberOfGeneratingVectors
	% Find all the translated edges in the zone for that generating vector.  This
	% information is just what DifferenceVectors recorded.
	Indices = find(DifferenceVectors == ctr)	;
	% Each translated edge starts at some initial vertex.  Find that set of vertices from
	% the information in the Edges matrix.
	InitialVertices = Edges(Indices,1)			;
	% Two edges, which are translations of the same generating vector, are part of the same
	% face if the vector difference between their initial vertices is a generating vector.
	% (In a zonohedron, all faces are parallelograms.)  Check through all pairs of 
	% edges (that are translations of the same generating vector) to find which pairs 
	% are opposite sides of a parallelogram, so belong to the same face.
	for idx1 = 1:length(InitialVertices)
		for idx2 = setdiff(1:length(InitialVertices),idx1)
			if ismember(transpose(InitialVertices([idx1,idx2])), Edges, 'rows')
				% Add the parallelogram to the list of faces.  Sort the vertices, so
				% that they can be compared later for duplicates
				Faces = [Faces; min(Edges(Indices(idx1),1), Edges(Indices(idx2),2)) ...
				                min(Edges(Indices(idx1),2), Edges(Indices(idx2),1))...
				                max(Edges(Indices(idx1),1), Edges(Indices(idx2),2)) ...
				                max(Edges(Indices(idx1),2), Edges(Indices(idx2),1))]	;
			end
		end
	end
end
% Eliminate duplicate faces
Faces = unique(Faces, 'rows')	;

if DisplayFigure
	FigureHandle = figure	;
	NumberOfFaces = size(Faces,1)	;
	for ctr = 1:NumberOfFaces
		plot3([Vertices(Faces(ctr,1),1),Vertices(Faces(ctr,2),1),Vertices(Faces(ctr,3),1),...
					Vertices(Faces(ctr,4),1),Vertices(Faces(ctr,1),1)], ...
			   [Vertices(Faces(ctr,1),2),Vertices(Faces(ctr,2),2),Vertices(Faces(ctr,3),2),...
					Vertices(Faces(ctr,4),2),Vertices(Faces(ctr,1),2)], ...	
			   [Vertices(Faces(ctr,1),3),Vertices(Faces(ctr,2),3),Vertices(Faces(ctr,3),3),...
					Vertices(Faces(ctr,4),3),Vertices(Faces(ctr,1),3)], 'k-')
		hold on	
	end
	set(gca,'dataaspectratio',[1 1 1])
else
	FigureHandle = -99	;	% Return flag that no figure was made
end

return