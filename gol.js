class GameOfLife {

	constructor(height, width){
		this.refreshRate = 500;
		this.simulating = false;
		this.height = height;
		this.width = width;

		this.lifeMap = new Array(height);
		this.lifeMap2 = new Array(height);
		for (var i = 0; i < height; i++)
		{
			this.lifeMap[i] = new Array(width);
			this.lifeMap2[i] = new Array(height);
		}

		this.clearLifeMap();
		this.clearLifeMap2();

		this.canvas = document.getElementById("fred");
		this.ctx=this.canvas.getContext("2d");



	}
  onClick()
  {
    alert(event.pageX + " , " + event.pageY);
  }

	clearLifeMap(){
		for (var i = 0; i < this.height; i++)
		{
			for(var j = 0; j < this.width; j++)
			{
				this.lifeMap[i][j] = false;
			}
		}
	}

	clearLifeMap2(){
		for (var i = 0; i < this.height; i++)
		{
			for(var j = 0; j < this.width; j++)
			{
				this.lifeMap2[i][j] = false;
			}
		}
	}

	alive(x,y){
		this.lifeMap[y][x] = true;
	}

	kill(x,y){
		this.lifeMap[y][x] = false;
	}


	copyLifeMap(){
        for (var i = 0; i < this.height; i++)
        {
            for (var j = 0; j < this.width; j++)
            this.lifeMap2[i][j] = this.lifeMap[i][j];

        }
    }

    clearCanvas()
    {
    	//  context.clearRect(0, 0, canvas.width, canva s.height);

    	this.canvas.width = this.canvas.width;



    }
//----------------------------
	symulate(){
		this.copyLifeMap();
		this.clearLifeMap();
			//alert(this.height);
			for(var wysokoscRS = 1; wysokoscRS < this.height - 1 ; wysokoscRS++)
		        {

		            for(var szerokoscRS = 1; szerokoscRS < this.width - 1 ; szerokoscRS++)
		            {
		                this.neighbors=0;

		                    //o o o
		                    if(this.lifeMap2[wysokoscRS+1][szerokoscRS-1]==true) this.neighbors++;
		                    if(this.lifeMap2[wysokoscRS+1][szerokoscRS]==true) this.neighbors++;
		                    if(this.lifeMap2[wysokoscRS+1][szerokoscRS+1]==true) this.neighbors++;
		                    //o X o
		                    if(this.lifeMap2[wysokoscRS][szerokoscRS-1]==true) this.neighbors++;
		                    if(this.lifeMap2[wysokoscRS][szerokoscRS+1]==true) this.neighbors++;
		                    //o o o
		                    if(this.lifeMap2[wysokoscRS-1][szerokoscRS-1]==true) this.neighbors++;
		                    if(this.lifeMap2[wysokoscRS-1][szerokoscRS]==true) this.neighbors++;
		                    if(this.lifeMap2[wysokoscRS-1][szerokoscRS+1]==true) this.neighbors++;

		                    //alert(szerokoscRS + " , " + wysokoscRS + " : " + this.neighbors);

		                    if(this.lifeMap2[wysokoscRS][szerokoscRS] == true)
		                    {
		                        if((this.neighbors == 3)||(this.neighbors == 2)) this.lifeMap[wysokoscRS][szerokoscRS] = true;
		                        else this.lifeMap[wysokoscRS][szerokoscRS] = false;

		                    }
		                    else
		                    {
		                         if(this.neighbors == 3)
		                          this.lifeMap[wysokoscRS][szerokoscRS] = true;
		                          else this.lifeMap[wysokoscRS][szerokoscRS] = false;

		                    }



		                //gotoXY(2, height+ iterator++);
		                //cout << "Komorka " << szerokoscRS << ", " << wysokoscRS << ". sasiedzi: " << neighbors;

		            }
		        }
		  this.clearLifeMap2();
		}

	drawSquare10(x,y){
		this.ctx.fillStyle = "#48af23";
		this.ctx.fillRect(x,y, 10,10);
		this.ctx.fillStyle="#48af23";
		this.ctx.rect(x,y,10,10);
	}

	draw(){
		this.clearCanvas();
		for(var i = 0; i < this.height; i++)
		{
			for(var j = 0; j < this.width; j++)
			{
				if(this.lifeMap[i][j]===true)
				{
					this.drawSquare10(j*10, i*10);
				}
			}
		}
		this.ctx.stroke();
	}

	cycle(){

	this.symulate();
	this.draw();

	}

	pauseUnpause(){
		this.simulating = !this.simulating;
		if(this.simulating) document.getElementById("pauseUnpause").innerHTML = "Pause";
		else document.getElementById("pauseUnpause").innerHTML = "Unpause";

	}


}
//--------------------------------------KONIEC KLASY----------------------------------------------------------------
/*
var canvas;
var ctx;
function init(){
canvas = document.getElementById("fred");
ctx = canvas.getContext("2d");
}
function drawSquare(x,y)
{
	ctx.rect(x*10,y*10,10,10);
	ctx.stroke();
}
*/
var GOL;
function start()
{

	GOL = new GameOfLife(80,100);

  cycle();
}

function cycle()
{
  if(GOL.simulating)
  {
  GOL.cycle();

}
setTimeout(cycle, GOL.refreshRate);
}

function pauseUnpause()
{
	GOL.pauseUnpause();
}

function changeRefreshRate()
{
  GOL.refreshRate = 1000 -  document.getElementById("myRange").value * 10;
  document.getElementById("speed").innerHTML = GOL.refreshRate;
}
function onClick(event)
{
  if(GOL.simulating) return;

  var canvasY= document.getElementById("fred").getBoundingClientRect().top;
  var canvasX= document.getElementById("fred").getBoundingClientRect().left;

  var x = event.clientX;
  var y = event.clientY;

  var arrayX = Math.floor((x - canvasX )/10);
  var arrayY = Math.floor((y - canvasY)/10);
//alert(arrayX + " , " + arrayY);

  GOL.lifeMap[arrayY][arrayX] = !GOL.lifeMap[arrayY][arrayX];
  GOL.draw();
}

function clearButton()
{
	if(GOL.simulating)
	pauseUnpause();

	GOL.clearLifeMap();
	GOL.draw();
	}
