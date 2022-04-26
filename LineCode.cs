using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LineCode : MonoBehaviour
{

    LineRenderer lineRenderer; 
    // Get the object, take the transform then take the line to attach to that sphere
    public Transform origin; //Starting keypoint point
    public Transform destination; // Ending point 

    // Start is called before the first frame update
    void Start()
    {
       lineRenderer = GetComponent<LineRenderer>();
       lineRenderer.startWidth = 0.1f;
       lineRenderer.endWidth = 0.1f;
        
    }

    // Update is called once per frame
    void Update()
    {
        // start and end point as origin position
        lineRenderer.SetPosition(0, origin.position); 
        lineRenderer.SetPosition(1, destination.position); 
        
    }
}
