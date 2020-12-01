import java.io.*;
import java.util.*;
public class MaxFlowGraphGenerator {

	public static void populateGraph(WGraph g, int n, int maxWeight) { //where N = 6n and min = 1
		ArrayList<Integer> n1_nodes = new ArrayList<Integer>(n);
		ArrayList<Integer> n1_colnodes = new ArrayList<Integer>(2*n);
		ArrayList<Integer> n2_colnodes = new ArrayList<Integer>(2*n);
		ArrayList<Integer> n2_nodes = new ArrayList<Integer>();
		int i;

		for (i = 0; i< n; i++) {
			n1_nodes.add(i);
		}
		//i==n now
		for (;i < 3*n; i++) {
			n1_colnodes.add(i);
		}
		//i==2n + (n-1)
		for (;i < 5*n; i++) {
			n2_colnodes.add(i);
		}
		for (;i < 6*n; i++) {
			n2_nodes.add(i);
		}
		
		for (int k = 0; k < n1_nodes.size(); k++) {
			if (k < n1_nodes.size() -1) {
				g.addEdge(new Edge(n1_nodes.get(k), n1_nodes.get(k+1), generateRandom(maxWeight)));
				if (n1_colnodes.get(0)> k+2) {
					g.addEdge(new Edge(n1_nodes.get(k), n1_nodes.get(k+2), generateRandom(maxWeight)));
				}else {
					g.addEdge(new Edge(n1_nodes.get(k), n1_colnodes.get(0), generateRandom(maxWeight)));
				}
			}else {
				g.addEdge(new Edge(n1_nodes.get(k), n2_colnodes.get(0), generateRandom(maxWeight)));
			}
			if (k == n1_nodes.size() -1) {
				g.addEdge(new Edge(n1_nodes.get(k), n1_colnodes.get(0), generateRandom(maxWeight)));
			}
			for (int j = 1; j < n1_colnodes.size(); j++) {
				if (n1_colnodes.get(j) != 3*n) {
				g.addEdge(new Edge(n1_nodes.get(k), n1_colnodes.get(j), generateRandom(maxWeight)));
				}
			}
			for (int j = 1; j < n2_colnodes.size(); j++) {
				if (n2_colnodes.get(j) != 3*n) {
				g.addEdge(new Edge(n1_nodes.get(k), n2_colnodes.get(j), generateRandom(maxWeight)));
				}
			}

		}
		
		for (int k = 0; k < n1_colnodes.size(); k++) {
			if (k==0) {
				g.addEdge(new Edge(n1_colnodes.get(k), n2_nodes.get(0), generateRandom(maxWeight)));
			}
			for (int j =0; j < n1_colnodes.size(); j++) {
				g.addEdge(new Edge(n1_colnodes.get(k), n2_colnodes.get(j), generateRandom(maxWeight)));
			}
			
		}
		g.addEdge(new Edge(n2_colnodes.get(0), n2_nodes.get(0), generateRandom(maxWeight)));
		if (n >= 2) {
			g.addEdge(new Edge(n2_colnodes.get(0), n2_nodes.get(1), generateRandom(maxWeight))); //need minimum n =2
		}
			
		for (int k = 1; k < n2_colnodes.size(); k++) {
			for (int j =0; j < n2_nodes.size(); j++) {
				g.addEdge(new Edge(n2_colnodes.get(k), n2_nodes.get(j), generateRandom(maxWeight)));
			}
		}
		
		for (int k = 0; k < n2_nodes.size()-1; k++) {
			g.addEdge(new Edge(n2_nodes.get(k), n2_nodes.get(k+1), generateRandom(maxWeight)));
			if (k+2 < n2_nodes.size()) {
				g.addEdge(new Edge(n2_nodes.get(k), n2_nodes.get(k+2), generateRandom(maxWeight)));
			}
		}

		


	}

	public static int generateRandom(int max) {     
		Random generator = new Random(); 
		int i = generator.nextInt(max-1-1);
		return i+1+1;     
	}


	public static void main(String[] args){
		Integer nodes =  Integer.parseInt(args[0]);
		Integer maxW = Integer.parseInt(args[1]);
		WGraph g = new WGraph();
		populateGraph(g,nodes,maxW);
		g.setDestination(g.getNbNodes()-1);		
		System.out.print(g.toString());

	}
}
