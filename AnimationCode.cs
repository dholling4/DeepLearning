using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using System.Threading;

public class AnimationCode : MonoBehaviour // Class AnimationCode is inheriting from MonoBehaviour (runs unity commands)
{
    // create list of game objects and store it to body 
    public GameObject[] Body;
    // grab each line and convert to numbers
    List<string> lines; 
    int counter = 0;
    // Start is called before the first frame update
    void Start()
    {
        lines = System.IO.File.ReadLines("Assets/David_arms_dark.txt").ToList();
        
    }

    // Update is called once per frame
    void Update()
    {
        string[] points = lines[counter].Split(',');

        for (int i = 0; i <= 32; i++)
        {
            float x = float.Parse(points[0 + (i * 3)]) / 100; 
            float y = float.Parse(points[1 + (i * 3)]) / 100;
            float z = float.Parse(points[2 + (i * 3)]) / 300;
            Body[i].transform.localPosition = new Vector3(x, y, z);
        }
        // save x, y, z points as float

        counter += 1; 
        if (counter == lines.Count) { counter = 0; }
        Thread.Sleep(30); // slow down by 30ms per frame
    }
}
