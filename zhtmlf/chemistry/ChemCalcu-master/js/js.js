window.onload=function(){
	var _periodTable=document.getElementById("periodTable");//获取元素周期表板块
	var _num=document.getElementById("num");//获取数字板块
	var chemElements=_periodTable.getElementsByTagName("button");//获取所有化学元素
	var _numvalue=_num.getElementsByClassName("numvalue");//获取原子/分子数
	var _operation=_num.getElementsByClassName("operation");
    var _inputbox=document.getElementById("inputbox");//获取输入框
    var _result=document.getElementById("result");//获取显示计算结果框
    var _calcu=document.getElementById("calcu");//获取计算按钮

	
	
	
	

	/*1、新建两个空数组，一个用来储存化学元素的分子量值、数字值Num[]；另一个用来储存化学元素符号、数字Symbol[]；
	  2、为页面中的按钮添加点击事件；
	  3、点击化学元素、数字的时候，将分子量的值、数字值储存在Num[]；将元素符号、数字储存在Symbol[]数组中；
	  4、将Num[]数组中的元素依次提取出来进行数值计算，并将计算结果赋予变量res；同时将Symbol[]数组符号、数字按照顺序依次排列，并将结果赋予info；
	  5、当点击“计算”按钮时，_result中显示info:res;
	*/
	var Num=[];
	var Symbol=[];
	
	for(i=0;i<chemElements.length;i++){
		chemElements[i].onclick=function(){
			//将化学元素的分子量储存在Num数组中
			var _chemElement=this.getElementsByTagName("span")[2].innerText;
			Num.push(_chemElement);
			//将化学元素的符号储存在Symbol数组中
			var _chemSymbol=this.getElementsByTagName("span")[1].innerText;
			Symbol.push(_chemSymbol);
			//将Num数组内的数字拆分成字符串，然后进行计算
			console.log(Num);
			var results="";
			var info="";
	        if(Num.length!=0){
		        for(j=0;j<Num.length;j++){
		            results+=Num[j];
		            _inputbox.value=results;				
	            }	            
	        }
	        if(Symbol.length!=0){
		        for(j=0;j<Symbol.length;j++){
		            info+=Symbol[j];
		            _result.value=info;				
	            }	            
	        }
			
			
			//oInput.value+=this.getElementsByTagName("span")[2].innerText;
			//oResult.innerHTML+=this.getElementsByTagName("span")[1].innerText;
		}
	}
	var Timer=null;

	for(i=0;i<_numvalue.length;i++){
		_numvalue[i].onclick=function(){
			var _this=this.innerText;
			clearTimeout(Timer);
			Timer=setTimeout(function(){
				Num.push("*"+_this);
				Symbol.push(_this.sub());
				console.log(Num);
			    var results="";
			    var info="";
	            if(Num.length!=0){
		            for(j=0;j<Num.length;j++){
		                results+=Num[j];
		                _inputbox.value=results;				
	                }	            
	            }
	            if(Symbol.length!=0){
		            for(j=0;j<Symbol.length;j++){
		                info+=Symbol[j];
		                _result.value=info;				
	                }	            
	            }
			},500);			
		}
		_numvalue[i].ondblclick=function(){
			var _this=this.innerText;
			clearTimeout(Timer);
			Num.push(_this+"*");
			Symbol.push(_this);
			console.log(Num);
			var results="";
	        if(Num.length!=0){
		        for(j=0;j<Num.length;j++){
		            results+=Num[j];
		            _inputbox.value=results;				
	            }	            
	        }
	        if(Symbol.length!=0){
		        for(j=0;j<Symbol.length;j++){
		            info+=Symbol[j];
		            _result.value=info;				
	            }	            
	        }
		}
	}

	for(i=0;i<_operation.length;i++){
		_operation[i].onclick=function(){
			var _this=this.innerText;
			if(_this=="+"){
				Num.push(_this);
				var results="";
	            if(Num.length!=0){
		            for(j=0;j<Num.length;j++){
		                results+=Num[j];
		                _inputbox.value=results;				
	                }	            
	            }
			}else if(_this=="("){
				Num.push(_this);
				var results="";
	            if(Num.length!=0){
		            for(j=0;j<Num.length;j++){
		                results+=Num[j];
		                _inputbox.value=results;				
	                }	            
	            }
			}else if(_this==")"){
				Num.push(_this);
				var results="";
	            if(Num.length!=0){
		            for(j=0;j<Num.length;j++){
		                results+=Num[j];
		                _inputbox.value=results;				
	                }	            
	            }
			}else if(_this=="C"){
				Num=[];
				_inputbox.value="";
				Symbol=[];
				_result.innerHTML="";
			}else if(_this=="←"){
				var info="";
	            if((Num[Num.length-1]!="+")&&(Num[Num.length-1]!="(")&&(Num[Num.length-1]!=")")){
	            	
	            	Symbol.splice(Symbol.length-1,Symbol.length);
	            	if(Symbol.length!=0){
		                for(j=0;j<Symbol.length;j++){
		                    info+=Symbol[j];
		                    _result.value=info;				
	                    }            
	                }
	            }
				Num.splice(Num.length-1,Num.length);
				var results="";
	            if(Num.length!=0){
		            for(j=0;j<Num.length;j++){
		                results+=Num[j];
		                _inputbox.value=results;				
	                }	            
	            }

	            
	            	
			}else if(_this=="·"){
				Num.push("+");
				var results="";
	            if(Num.length!=0){
		            for(j=0;j<Num.length;j++){
		                results+=Num[j];
		                _inputbox.value=results;				
	                }	            
	            }
			}
		}
	}


	//点击计算按钮就可以显示结果
	_calcu.onclick=function(){
		var str2=_inputbox.value;
		_result.innerHTML=_result.value+":"+eval(str2).toFixed(2);

    }
}