// 要操作的元素
let play_pause = document.querySelector('.play-pause'),
	player_track = document.querySelector('.player-track'),
	album_cover = document.querySelector('.album-cover'),
	bg = document.querySelector('.bg'),
	album_name = document.querySelector('.album-name'),
	track_name = document.querySelector('.track-name'),
	track_time = document.querySelector('.track-time'),
	current_time = document.querySelector('.current-time'),
	total_time = document.querySelector('.total-time'),
	progress_box = document.querySelector('.progress-box'),
	hover_time = document.querySelector('.hover-time'),
	progress_bar = document.querySelector('.progress-bar'),
	player_content = document.querySelector('.player-content'),
	play_prev = document.querySelector('.play-prev'),
	play_next = document.querySelector('.play-next'),
	play_select = document.querySelector('.play-select'),
	play_select_label = document.querySelector('.play-select>label'),
	play_controlsTwo = document.querySelector('.play-controlsTwo'),
	play_controlsTwo_input = document.querySelector('.play-controlsTwo>label>input');

// 动漫歌曲播放记录
let comic_name = new Array();
// 歌曲信息数组
let track_names = ["METAMORPHOSIS - INTERWORLD",
"Murder In My Mind (Slowed + Reverb)",
"周杰伦 - 本草纲目",
"周深 - 大鱼",
"温亮亮 - 相信我们会创造奇迹",
"鞠婧祎 - 红昭愿 (Live)"];

// 定义变量
let progress_t, //鼠标在进度条上悬停的位置
	progress_loc, //鼠标在进度条上悬停的音频位置
	c_m, //悬停音频位置(分钟)
	ct_minutes, //悬停播放位置(分)
	ct_seconds, //悬停播放位置(秒)
	cur_minutes, //当前播放时间(分)
	cur_seconds, //当前播放时间(秒)
	dur_minutes, //音频总时长(分)
	dur_seconds, //音频总时长(秒)
	play_progress, //播放进度
	State = false, //播放状态
	labelInput = false, //播放哪种歌曲
	jilushu = 0; //记录动漫记录中的上下首

// 初始化歌曲下标
const array = new Uint32Array(1);
maxUint = 0xffffffff //maxUint为最大的可能值
const randomNum = crypto.getRandomValues(array)[0] / maxUint;
let cur_index = Math.floor((4 - 0 + 1) * randomNum + 0) - 1;

// 初始化
function initPlayer() {
	audio = new Audio(); //创建音频对象
	audio.loop = false; //不循环播放
	selectTrack(0);
	// 绑定播放暂停按钮的点击事件
	play_pause.addEventListener('click', playPause);
	// 进度条鼠标移动事件
	progress_box.addEventListener('mousemove', function(e) {
		showHover(e);
	});
	// 进度条鼠标离开事件
	progress_box.addEventListener('mouseout', hideHover);
	// 进度条点击事件
	progress_box.addEventListener('click', playFromClickedPos);
	// 音频播放位置改变事件
	audio.addEventListener('timeupdate', updateCurTime);
	// 上一首按钮点击事件
	play_prev.addEventListener('click', function() {
		selectTrack(-1);
	});
	// 下一首按钮点击事件
	play_next.addEventListener('click', function() {
		selectTrack(1);
	});
	play_select.addEventListener('click', UIadjustment);
	play_controlsTwo_input.addEventListener('change', networkingANDswitch);
}

//判断设备是否联网，动漫歌曲开关是否打开
function networkingANDswitch() {
	if (this.checked === true) {
		if (navigator.onLine) { //正常工作
			labelInput = true;
		} else { //执行离线状态时的任务
			this.checked = false;
			alert('你的设备未联网');
		}
	} else {
		labelInput = false;
	}
	if (audio.currentTime == 0 && audio.paused === true)
		selectTrack(1);
}

//单击菜单时调整界面
function UIadjustment() {
	if (play_select_label.className == 'SelectYse') {
		play_select_label.classList.remove('SelectYse');
		play_select_label.classList.add('SelectNo');
		player_content.style.height = '158%';
		setTimeout(function() {
			play_controlsTwo.style.display = 'flex';
		}, 300);
	} else {
		play_select_label.classList.remove('SelectNo');
		play_select_label.classList.add('SelectYse');
		play_controlsTwo.style.display = 'none';
		player_content.style.height = '100%';
	}
}

// 播放暂停
function playPause() {
	setTimeout(function() {
		if (audio.paused) {
			player_track.classList.add('active');
			play_pause.querySelector('.fa').classList = 'fa fa-pause';
			album_cover.classList.add('active');
			audio.play();
			State = true;
		} else {
			player_track.classList.remove('active');
			play_pause.querySelector('.fa').classList = 'fa fa-play';
			album_cover.classList.remove('active');
			audio.pause();
			State = false;
		}
	}, 100);
}

// 显示悬停播放位置弹层
function showHover(e) {
	// 计算鼠标在进度条上的悬停位置(当前鼠标的X坐标-进度条在窗口中的left位置)
	progress_t = e.clientX - progress_box.getBoundingClientRect().left;
	// 计算鼠标在进度条上悬停时的音频位置
	// audio.duration 音频总时长
	progress_loc = audio.duration * (progress_t / progress_box.getBoundingClientRect().width);
	// 将悬停音频位置转为分钟
	c_m = progress_loc / 60;
	ct_minutes = Math.floor(c_m); //分
	ct_seconds = Math.floor(progress_loc - ct_minutes * 60); //秒
	if (ct_minutes < 10) {
		ct_minutes = '0' + ct_minutes;
	}
	if (ct_seconds < 10) {
		ct_seconds = '0' + ct_seconds;
	}
	if (isNaN(ct_minutes) || isNaN(ct_seconds)) {
		hover_time.innerText = '--:--';
	} else {
		hover_time.innerText = ct_minutes + ':' + ct_seconds;
	}
	// 设置悬停播放位置弹层的位置并显示
	hover_time.style.left = progress_t + 'px';
	hover_time.style.marginLeft = '-20px';
	hover_time.style.display = 'block';
}

// 隐藏悬停播放位置弹层
function hideHover() {
	hover_time.innerText = '00:00';
	hover_time.style.left = '0px';
	hover_time.style.marginLeft = '0px';
	hover_time.style.display = 'none';
}

// 从点击的位置开始播放
function playFromClickedPos() {
	// 设置当前播放时间
	audio.currentTime = progress_loc;
	// 设置进度条宽度
	progress_bar.style.width = progress_t + 'px';
	// 隐藏悬停播放位置弹层
	hideHover();
}

// 改变当前播放时间
function updateCurTime() {
	// 当前播放时间(分)
	cur_minutes = Math.floor(audio.currentTime / 60);
	// 当前播放时间(秒)
	cur_seconds = Math.floor(audio.currentTime - cur_minutes * 60);
	// 音频总时长(分)
	dur_minutes = Math.floor(audio.duration / 60);
	// 音频总时长(秒)
	dur_seconds = Math.floor(audio.duration - dur_minutes * 60);
	// 计算播放进度
	play_progress = audio.currentTime / audio.duration * 100;
	cur_minutes = cur_minutes < 10 ? '0' + cur_minutes : cur_minutes;
	cur_seconds = cur_seconds < 10 ? '0' + cur_seconds : cur_seconds;
	dur_minutes = dur_minutes < 10 ? '0' + dur_minutes : dur_minutes;
	dur_seconds = dur_seconds < 10 ? '0' + dur_seconds : dur_seconds;
	// 设置播放时间
	if (isNaN(cur_minutes) || isNaN(cur_seconds)) {
		current_time.innerText = '00:00';
	} else {
		current_time.innerText = cur_minutes + ':' + cur_seconds;
	}
	// 设置总时长
	if (isNaN(dur_minutes) || isNaN(dur_seconds)) {
		total_time.innerText = '00:00';
	} else {
		total_time.innerText = dur_minutes + ':' + dur_seconds;
	}
	// 设置进度条宽度
	progress_bar.style.width = play_progress + '%';
	// 播放完毕
	if (play_progress == 100) {
		//自动播放下一首
		selectTrack(1);
		//恢复样式
		// play_pause.querySelector('.fa').classList='fa fa-play';
		// progress_bar.style.width='0px';
		// current_time.innerText='00:00';
		// player_track.classList.remove('active');
		// album_cover.classList.remove('active');
	}
}

// 切换歌曲(flag: 0=初始, 1=下一首, -1=上一首)
function selectTrack(flag) {
	if (labelInput === false) {
		if (flag == 0 || flag == 1) {
			if (cur_index == (track_names.length - 1)) {
				cur_index = 0;
			} else {
				++cur_index;
			}
		} else {
			if (cur_index == 0) {
				cur_index = (track_names.length - 1);
			} else {
				--cur_index;
			}
		}
		if (cur_index > -1 && cur_index < track_names.length) {
			try {
				if (flag == 0) {
					play_pause.querySelector('.fa').classList = 'fa fa-play';
				} else if (State == true) {
					play_pause.querySelector('.fa').classList = 'fa fa-pause';
				}
				progress_bar.style.width = '0px';
				current_time.innerText = '00:00';
				total_time.innerText = '00:00';
				// 当前专辑名
				let cur_album = track_names[cur_index];
				// 当前歌曲信息(歌手 - 歌名)
				let cur_track_name = track_names[cur_index];
				// 设置音频路径和判断文件是否正常加载
				audio.src = '../mp3/' + cur_album + '.mp3?PC' + new Date().getTime();
				setTimeout(function() {
					if (audio.readyState == 0) {
						audio.src = '../wav/' + cur_album + '.wav?PC' + new Date().getTime();
						setTimeout(function() {
							if (audio.readyState == 0) {
								audio.src = '../flac/' + cur_album + '.flac?PC' + new Date().getTime();
								setTimeout(function() {
									if (audio.readyState == 0) {
										selectTrack(1);
									} else {
										AudioNormal();
									}
								}, 333);
							} else {
								AudioNormal();
							}
						}, 333);
					} else {
						AudioNormal();
					}
				}, 334);
				// audio.onerror=function(){}
				function AudioNormal() {
					// 当切换上一首,下一首时,判断是否播放
					if (flag != 0 && State == true) {
						audio.play();
					}
					// 设置专辑名
					album_name.innerText = cur_album;
					// 设置歌曲信息
					track_name.innerText = cur_track_name;
					// 设置封面
					document.querySelector('img').src = '../image/' + cur_album + '.jpg';
					// 将封面设置为背景大图
					bg.style.backgroundImage = 'url(' + document.querySelector('img').src + ')';
					document.querySelector('img').onerror = function() {
						// 设置封面
						document.querySelector('img').src = '../image/迷你音乐.png';
						// 将封面设置为背景大图
						bg.style.backgroundImage = 'url(' + document.querySelector('img').src + ')';
						throw new Error('图片路径有误');
					}
				}
			} catch (e) {
				console.log('程序抛出异常');
			}
		} else {
			// 切换溢出专辑数组时, 恢复cur_index
			if (flag == 0 || flag == 1) {
				--cur_index;
			} else {
				++cur_index;
			}
		}
	} else {
		if (flag == 0 || flag == 1) {
			if (jilushu >= comic_name.length) {
				$.ajax({
					type: 'GET',
					url: 'https://anime-music.jijidown.com/api/v2/music',
					success: function(msg) {
						audio.src = msg.res.play_url;
						if (State == true) {
							audio.play();
						}
						// 设置专辑名
						album_name.innerText = msg.res.title;
						// 设置歌曲信息
						track_name.innerText = msg.res.title;
						let comic_names = {
							title: msg.res.title,
							url: msg.res.play_url
						};
						comic_name.push(comic_names);
						jilushu = comic_name.length;
					}
				});
			} else {
				audio.src = comic_name[jilushu].url;
				if (State == true) {
					audio.play();
				}
				// // 设置专辑名
				album_name.innerText = comic_name[jilushu].title;
				// // 设置歌曲信息
				track_name.innerText = comic_name[jilushu].title;
				jilushu += 1;
			}
		} else {
			if (jilushu - 2 >= 0) {
				audio.src = comic_name[jilushu - 2].url;
				if (State == true) {
					audio.play();
					player_track.classList.add('active');
					album_cover.classList.add('active');
				}
				// // 设置专辑名
				album_name.innerText = comic_name[jilushu - 2].title;
				// // 设置歌曲信息
				track_name.innerText = comic_name[jilushu - 2].title;
				jilushu -= 1;
			}
		}
		document.querySelector('img').src = '../image/迷你音乐.png';
		bg.style.backgroundImage = 'url(../image/迷你音乐.png)';
	}
}

// 初始化播放器
initPlayer();
